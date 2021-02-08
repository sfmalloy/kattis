#include <iostream>
#include <map>
#include <cmath>
#include <vector>

int main() {
    size_t n;
    std::cin >> n;

    while(n != 0) {
        std::map<unsigned, std::vector<std::string>> names;
        for (size_t i = 0; i < n; ++i) {
            std::string curr;
            std::cin >> curr;

            unsigned weight = (unsigned) pow(curr[0], 2) + curr[1];
            names[weight].push_back(curr);
        }

        for (const auto& p : names) {
            for (const std::string& s : p.second) {
                std::cout << s << '\n';
            }
        }

        std::cout << '\n';
        std::cin >> n;
    }
    
    return 0;
}
