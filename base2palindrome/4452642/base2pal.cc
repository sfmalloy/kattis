#include <iostream>
#include <bitset>
#include <cmath>

template<size_t size>
bool isPalindrome(const std::bitset<size>& base2, size_t end);

int main() {
    int M;
    std::cin >> M;

    if (M == 1) {
        std::cout << 1 << '\n';
    } else if (M == 2) {
        std::cout << 3 << '\n';
    } else {
        unsigned long long x = log2(M + 1), zeros = 2 * x - 3;
        int m = pow(2, x) - 1;

        unsigned long long m_check = (m + (2 * (m + 1))) / 2;
        if (M >= m_check) {
            m = m_check;
            ++zeros;
        }

        unsigned long long base10 = pow(2, zeros + 1) + 1;
        size_t bitSize = zeros + 2;

        std::bitset<32> base2;
        for ( ; m <= M; ++m, base10 += 2) {
            base2 = base10;

            if (!isPalindrome<base2.size()>(base2, bitSize))
                --m;

            if (base2.count() == bitSize)
                ++bitSize;
        }

        std::cout << base2.to_ullong() << '\n';
    }

    return 0;
}

template<size_t size>
bool isPalindrome(const std::bitset<size>& base2, size_t end) {
    for (size_t i = 1; i <= (end - 1) / 2; ++i) {
        if (base2[i] != base2[end - i - 1])
            return false;
    }

    return true;
}