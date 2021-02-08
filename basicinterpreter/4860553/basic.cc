#include <iostream>
#include <map>
#include <unordered_map>
#include <string>
#include <cctype>
#include <array>

// Returns result of computing expression.
int eval(std::string expression, const std::unordered_map<char, int>& vars);

// Returns GOTO label if expression is true, otherwise -1.
int test(std::string expression, const std::unordered_map<char, int>& vars);

// Returns value represented by string x, which can either be a character
// representing a variable, or a 32-bit signed integer.
int get_value(std::string x, const std::unordered_map<char, int>& vars);

// Prints expression to console.  If a literal string, removes quotes.
void print(std::string expression, const std::unordered_map<char, int>& vars, bool new_line);

struct Command {
    std::string keyword, expression;
};

int main() {
    // Parses input and strips label from line and splits command into
    // a keyword and expreession.  Each line is put into a map which is mapped
    // by its corresponding label number.
    std::map<int, Command> lines;
    std::string input;
    while (std::getline(std::cin, input)) {
        int split_index = input.find(" "), label = std::stoi(input.substr(0, split_index));
        std::string rest = input.substr(split_index + 1);

        split_index = rest.find(" ");
        Command c;
        c.keyword = rest.substr(0, split_index);
        c.expression = rest.substr(split_index + 1);
        
        lines[label] = c;
    }


    // Execute BASIC program by iterating through lines and calling functions
    // based on keywords.  lines.begin() is the command with the smallest
    // label, and lines.end() - 1 is the command with the largest label.
    std::unordered_map<char, int> vars;
    for (auto i = lines.begin(), next_i = lines.begin(); i != lines.end(); i = next_i) {
        ++next_i;
        if (i->second.keyword == "LET") {
            vars[i->second.expression[0]] = eval(i->second.expression.substr(4), vars);
        } else if (i->second.keyword == "IF") {
            int goto_label = test(i->second.expression, vars);
            if (goto_label != -1) {
                next_i = lines.find(goto_label);
            }
        } else if (i->second.keyword == "PRINT") {
            print(i->second.expression, vars, false);
        } else {
            print(i->second.expression, vars, true);
        }
    }

    return 0;
}

// Returns result of computing expression.
int eval(std::string expression, const std::unordered_map<char, int>& vars) {
    size_t split_index = expression.find(" ");
    
    if (split_index == std::string::npos) {
        return get_value(expression, vars);
    } else {
        std::string first = expression.substr(0, split_index);
        expression = expression.substr(split_index + 1);

        char op = expression[0];
        std::string second = expression.substr(2);
        
        int a = get_value(first, vars), b = get_value(second, vars);

        if (op == '+') {
            return a + b;
        } else if (op == '-') {
            return a - b;
        } else if (op == '*') {
            return a * b;
        } else {
            return a / b;
        }
    }
}

// Returns GOTO label if expression is true, otherwise -1.
int test(std::string expression, const std::unordered_map<char, int>& vars) {
    std::array<std::string, 4> split_expression;
    for (int i = 0; i < 4; ++i) {
        size_t split_index = expression.find(" ");
        if (split_index != std::string::npos) {
            std::string temp = expression.substr(0, split_index);
            if (temp != "THEN" && temp != "GOTO") {
                split_expression[i] = expression.substr(0, split_index);
            } else {
                --i;
            }

            expression = expression.substr(split_index + 1);
        } else {
            split_expression[i] = expression;
        }
    }
    
    int a = get_value(split_expression[0], vars), b = get_value(split_expression[2], vars);
    std::string comp = split_expression[1];

    bool t = false;
    if (comp == "=" && a == b) {
        t = true;
    } else if (comp == ">" && a > b) {
        t = true;
    } else if (comp == "<" && a < b) {
        t = true;
    } else if (comp == "<>" && a != b) {
        t = true;
    } else if (comp == "<=" && a <= b) {
        t = true;
    } else if (comp == ">=" && a >= b) {
        t = true;
    }

    return t ? std::stoi(split_expression[3]) : -1;
}

// Returns value represented by string x, which can either be a character
// representing a variable, or a 32-bit signed integer.
int get_value(std::string x, const std::unordered_map<char, int>& vars) {
    return (std::isalpha(x[0]) ? vars.at(x[0]) : std::stoi(x));
}

void print(std::string expression, const std::unordered_map<char, int>& vars, bool new_line) {
    if (expression[0] == '\"') {
        std::cout << expression.substr(1, expression.size() - 2);
    } else {
        std::cout << vars.at(expression[0]);
    }

    if (new_line) {
        std::cout << '\n';
    }
}
