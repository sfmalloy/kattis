#include <iostream>
#include <vector>

int
sumSquareDigits(const int& base, int decimal);

int
main(int argc, char* argv[])
{
    unsigned cases;
    std::cin >> cases;

    unsigned n = 0;
    std::vector<int> sums;

    while (n < cases)
    {
        int base, decimal;
        std::cin >> n >> base >> decimal;
        sums.push_back(sumSquareDigits(base, decimal));
    }

    for (size_t i = 0; i < sums.size(); ++i)
        printf("%lu %d\n", i + 1, sums[i]);

    return 0;
}

int
sumSquareDigits(const int& base, int decimal)
{
    int sum = 0;
    while (decimal > 0)
    {
        int digit = decimal % base;
        sum += digit * digit;
        decimal /= base;
    }

    return sum;
}