#include <iostream>
#include <string>

int main()
{
    std::string hey;
    std::cin >> hey;

    std::cout << "h" << hey.substr(1, hey.size() - 2) << hey.substr(1, hey.size() - 2) << "y\n";

    return 0;
}
