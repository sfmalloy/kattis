#include <iostream>
#include <vector>

int main() {
    int b, c, d, l;
    std::cin >> b >> c >> d >> l;

    int count = 0;

    for (int i = 0; i * b <= l; ++i) {
        for (int j = 0; j * c <= l; ++j) {
            for (int k = 0; k * d <= l; ++k) {
                int l1 = i * b, l2 = j * c, l3 = k * d;
                if (l1 + l2 + l3 == l) {
                    ++count;
                    std::cout << i << ' ' << j << ' ' << k << '\n';
                }
            }
        }
    }

    if (count == 0)
        std::cout << "impossible\n";
    return 0;
}   
