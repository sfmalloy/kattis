#include <iostream>
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::to_string;

int
main(int argc, char* argv[])
{
    int n;
    cin >> n;

    bool goodCount = true;
    for (int i = 1; i <= n; ++i)
    {
        string input;
        cin >> input;

        goodCount = goodCount && (input == "mumble" || input == to_string(i));
    }

    cout << (goodCount ? "makes sense" : "something is fishy") << endl;

    return 0;
}