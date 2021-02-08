#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

int main() {
    size_t n;
    std::string code, guess;
    std::cin >> n >> code >> guess;

    size_t r = 0;
    std::unordered_map<char, int> codeMap;
    std::vector<size_t> skip;
    for (size_t i = 0; i < n; ++i) {
        if (code[i] == guess[i]) {
            ++r;
            skip.push_back(i);
        } else {
            ++codeMap[code[i]];
        }
    }

    size_t skipIndex = 0, s = 0;
    for (size_t k = 0; k < n; ++k) {
        if (skip.size() == 0 || k != skip[skipIndex]) {
            if (codeMap[guess[k]] > 0) {
                ++s;
                --codeMap[guess[k]];
            }
        } else {
            ++skipIndex;
        }
    }

    std::cout << r << ' ' << s << '\n';

    return 0;
}
