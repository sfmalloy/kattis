#include <iostream>
#include <string>
#include <map>

int main() {
    std::map<char, int> same;
    for (size_t i = 0; i < 5; ++i) {
        std::string curr;
        std::cin >> curr;
        ++same[curr[0]];
    }

    std::pair<char, int> max = {'Q', 0};
    for (auto& p : same) {
        if (p.second > max.second) {
            max = p;
        }
    }

    std::cout << max.second << '\n';

    return 0;
}
