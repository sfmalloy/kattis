#include <iostream>

int main() {
    
    int n;
    std::cin >> n;
    if (n % 2 == 1)
        std::cout << "Either\n";
    else if (n == 2 || n == 6 || n == 10)
        std::cout << "Odd\n";
    else if (n == 4 || n == 8)
        std::cout << "Even\n";

    return 0;
}
