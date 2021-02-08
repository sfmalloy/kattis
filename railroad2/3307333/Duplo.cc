#include <iostream>

using std::cout;
using std::cin;
using std::endl;

int
main(int argc, char* argv[])
{
    int x, y;
    cin >> x >> y;

    cout << ((y % 2 == 0) ? "possible" : "impossible") << endl;
}