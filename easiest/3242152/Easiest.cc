#include <iostream>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::vector;

int
sumOfDigits(int x);

int
main(int argc, char* argv[])
{
    int N = 1;
    vector<int> pList;

    while (N != 0)
    {
        cin >> N;
    
        int sum = sumOfDigits(N);

        int p;
        for (p = 11; sumOfDigits(p * N) != sum; ++p) {}

        pList.push_back(p);
    }

    pList.pop_back();

    for (const int& p : pList)
    {
        cout << p << endl;
    }

    return 0;
}

int
sumOfDigits(int x)
{
    int sum = 0;
    while (x > 0)
    {
        sum += x % 10;
        x /= 10;
    }

    return sum;
}