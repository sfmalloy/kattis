#include <iostream>
#include <vector>
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::string;
using std::to_string;

string
getSum(int max, bool even, bool odd);

int
main(int argc, char* argv[])
{
    int P;
    cin >> P;

    vector<string> sums;

    for (int i = 0; i < P; ++i)
    {
        int k, n;
        cin >> k >> n;
        sums.push_back(to_string(k) + " " + getSum(n + 1, 0, 0) + " " + getSum((n * 2) + 1, 0, 1) + " " + getSum((n * 2) + 1, 1, 0));
    }

    for (const string& sum : sums)
        cout << sum << endl;

    return 0;
}

string
getSum(int max, bool even, bool odd)
{
    long int sum = 0;
    for (int i = 0; i < max; ++i)
    {
        sum += i;
        if ((even && (i % 2 != 0)) || (odd && (i % 2 == 0)))
            sum -= i;
    }

    return to_string(sum);
}