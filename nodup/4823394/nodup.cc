#include <iostream>
#include <unordered_set>
#include <string>

int main() {
    std::unordered_set<std::string> words;
    std::string curr, response = "yes";
    bool reading = true;
    while (!std::cin.eof() && reading) {
        std::cin >> curr;
        if (!std::cin.eof() && !words.insert(curr).second) {
            response = "no";
            reading = false;
        }
    }

    std::cout << response << '\n';

    return 0;
}
