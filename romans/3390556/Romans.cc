#include <iostream>
#include <math.h>

using std::cout;
using std::cin;
using std::endl;

int
main(int argc, char* argv[])
{
    double f;
    cin >> f;

    f *= 1000.0 * (5280.0 / 4854.0);
    int newF = round(f);

    cout << newF << endl;

    return 0;
}