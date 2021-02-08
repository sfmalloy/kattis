#include <iostream>
#include <unordered_set>

int main() {
    int T;
    std::cin >> T;

    std::string city;
    for (int i = 0; i < T; ++i) {
        int N;
        std::cin >> N;
        std::unordered_set<std::string> cities;
        
        for (int j = 0; j < N; ++j) {
            std::cin >> city;
            cities.insert(city);
        }

        std::cout << cities.size() << std::endl;
    }
}
