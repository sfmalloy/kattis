#include <iostream>
#include <cmath>

int main() {
    int n;
    std::cin >> n;

    int new_num = 0;
    for (int p = log2(n), pow2 = pow(2, p); p >= 0; --p, pow2 /= 2)  {
        new_num += (n % 2) * pow2;
        n /= 2;
    }

    std::cout << new_num << std::endl;

    return 0;
}
