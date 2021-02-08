#include <iostream>
#include <string>
#include <unordered_set>

int main() {
    size_t P, N;
    std::cin >> P >> N;

    std::unordered_set<std::string> parts;
    int paradoxDay = 0;

    for (size_t i = 0; i < N; ++i) {
        std::string curr;
        std::cin >> curr;

        parts.insert(curr);

        if (parts.size() == P && paradoxDay == 0) {
            paradoxDay = i + 1;
        }
    }

    std::cout << (parts.size() == P ? std::to_string(paradoxDay) : "paradox avoided");

    return 0;
}