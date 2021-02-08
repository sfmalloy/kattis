#include <iostream>
#include <math.h>

#define _USE_MATH_DEFINES

int
main(int argc, char* argv[])
{
    int h, v;
    std::cin >> h >> v;
    std::cout << ceil(h / sin((v * M_PI) / 180)) << std::endl;

    return 0;
}