#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

int main() {
    std::string input;
    std::cin >> input;

    std::unordered_map<char, int> cardCounts;
    for (const auto& c : input) {
        ++cardCounts[c];
    }

    int sum = 0; 
    if (cardCounts.size() == 3) {
        sum = 7 * std::min(cardCounts['T'], std::min(cardCounts['C'], cardCounts['G']));
    }

    for (const auto& p : cardCounts) {
        sum += p.second * p.second;
    }

    std::cout << sum << std::endl;

    return 0;
}
