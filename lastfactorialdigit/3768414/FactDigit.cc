#include <iostream>
#include <vector>

int main() {
    size_t k;
    std::cin >> k;

    std::vector<int> digits;

    for (size_t i = 0; i < k; ++i) {
        int n;
        std::cin >> n;

        int digit;

        if (n < 3 || n == 4) {
            digit = n;
        } else if (n == 3) {
            digit = 6;
        } else {
            digit = 0;
        }

        digits.push_back(digit);
    }

    for (const int& d : digits) {
        std::cout << d << std::endl;
    }
    
    return 0;
}