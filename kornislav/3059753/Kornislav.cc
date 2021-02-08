#include <iostream>
#include <math.h>
#include <algorithm>

int
main (int argc, char* argv[])
{
    int a, b, c, d;
    std::cin >> a >> b >> c >> d;

    int nums[] {a, b, c, d};
    std::sort (nums, nums + 4);
    
    int area = std::min (nums[0], nums[1]) * std::min (nums[2], nums[3]);

    std::cout << area << std::endl;

    return 0;
}