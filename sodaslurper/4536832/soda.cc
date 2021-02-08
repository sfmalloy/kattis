#include <iostream>

int main() {
    int e, f, price;
    std::cin >> e >> f >> price;
    
    int sodaTotal = e + f, drank = 0;

    for ( ; sodaTotal >= price; ++drank) {
        sodaTotal -= price;
        ++sodaTotal;
    }

    std::cout << drank << '\n';
        
    return 0;
}
