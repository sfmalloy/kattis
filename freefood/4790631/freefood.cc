#include <iostream>
#include <unordered_set>

int main() {
    int N;
    std::cin >> N;

    std::unordered_set<int> days;
    for (int i = 0; i < N; ++i) {
        int high, low;
        std::cin >> low >> high;

        for (int j = low; j <= high; ++j) {
            days.insert(j);
        }
    }

    std::cout << days.size() << '\n';

    return 0;
}
