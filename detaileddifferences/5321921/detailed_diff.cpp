#include <iostream>
#include <string>

int main() {
    int cases;
    std::cin >> cases;

    for (int i = 0; i < cases; ++i) {
        std::string a,b;
        std::cin >> a >> b;
        
        std::cout << a << '\n' << b <<"\n";

        for (size_t j = 0; j < a.size(); ++j)
            std::cout << (a[j] == b[j] ? '.' : '*');
        
        std::cout << "\n\n";
        
        
    }

    return 0;
}