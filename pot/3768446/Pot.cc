#include <iostream>
#include <cmath>

int main() {
    size_t N;
    std::cin >> N;

    unsigned long sum = 0;

    for (size_t i = 0; i < N; ++i) {
        int num;
        std::cin >> num;

        int p = num % 10;
        num /= 10;

        sum += std::pow(num, p);
    }

    std::cout << sum;

    return 0;
}