#include <iostream>
#include <unordered_set>

int main() {
    int r, n;
    std::cin >> r >> n;

    std::unordered_set<int> booked;
    for (int i = 0; i < n; ++i) {
        int k;
        std::cin >> k;
        booked.insert(k);
    }

    int vacant = -1;
    for (int i = 1; vacant == -1 && i <= r; ++i) {
        if (booked.find(i) == booked.end())
            vacant = i;
    }

    if (vacant != -1)
        std::cout << vacant << '\n';
    else
        std::cout << "too late\n";

    return 0;
}
