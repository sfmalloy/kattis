#include <iostream>
#include <map>

using std::cout;
using std::cin;
using std::endl;
using std::map;

int
main(int argc, char* argv[])
{
    map<int, int> mods;

    for (int i = 0; i < 10; ++i)
    {
        int x;
        cin >> x;
        ++mods[x % 42];
    }

    cout << mods.size() << endl;

    return 0;
}