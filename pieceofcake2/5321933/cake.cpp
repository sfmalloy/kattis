#include <iostream>
#include <algorithm>

int main() {
    int n, h, v;
    std::cin >> n >> h >> v;

    int s1 = std::max(h, n - h), s2 = std::max(v, n - v);

    std::cout << s1 * s2 * 4 << '\n';

    return 0;
}