#include <iostream>
#include <stack>
#include <queue>
#include <vector>

inline int index(char letter)
{
    return letter - 65;
}

int main()
{
    int N;
    std::cin >> N;

    std::vector<bool> values;
    char c;
    for (int i = 0; i < N; ++i)
    {
        std::cin >> c;
        values.push_back(c == 'T');
    }

    std::queue<char> tokens;
    while (std::cin >> c)
        tokens.push(c);
    
    std::stack<bool> bools;
    while (tokens.size() > 0)
    {
        while (isalpha(tokens.front()))
        {
            bools.push(values[index(tokens.front())]);
            tokens.pop();
        }
        bool a = bools.top();
        bools.pop();

        if (tokens.size() > 0)
        {
            if (tokens.front() == '+')
            {
                bool b = bools.top();
                bools.pop();
                bools.push(b || a);
            }
            else if (tokens.front() == '*')
            {
                bool b = bools.top();
                bools.pop();
                bools.push(b && a);
            }
            else
                bools.push(!a);
            tokens.pop();
        }
        else
            bools.push(a);
    }

    std::cout << (bools.top() ? 'T' : 'F') << '\n';

    return 0;
}