#include <iostream>

int main() {
    int l, r;
    std::cin >> l >> r;

    if (l == 0 && r == 0) {
        std::cout << "Not a moose\n";
    } else if (l == r) {
        std::cout << "Even " << 2 * l << '\n';
    } else {
        std::cout << "Odd " << (l > r ? 2 * l : 2 * r) << '\n';
    }

    return 0;
}
