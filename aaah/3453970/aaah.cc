#include <iostream>

int 
main(int argc, char* argv[]) 
{
    std::string a, b;
    std::cin >> a >> b;

    if (a.size() < b.size())
        std::cout << "no";
    else
        std::cout << "go";

    return 0;
}