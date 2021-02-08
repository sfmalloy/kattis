#include <iostream>
#include <algorithm>
#include <vector>

int main() {
    std::string strN;
    std::getline(std::cin, strN);

    int n = std::stoi(strN);

    std::vector<std::string> lines(n);
    for (int i = 0; i < n; ++i) {
        std::getline(std::cin, lines[i]);
    }

    for (int i = 0; i < n; ++i) {
        if (lines[i].substr(0, 10) == "Simon says") {
            std::cout << lines[i].substr(10) << '\n';
        }
    }

    return 0;
}
