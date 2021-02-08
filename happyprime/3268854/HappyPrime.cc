#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

struct Case
{
    int caseNum;
    int happyNum;
    bool isHappy;
};

bool 
testHappiness(int happyNum);

int
happySum(int k);

bool
isPrime(int k);

int
main (int argc, char* argv[])
{
    size_t cases;
    cin >> cases;

    vector<Case> happyNums;
    
    for (size_t i = 0; i < cases; ++i)
    {
        int caseNum;
        cin >> caseNum;

        int happyNum;
        cin >> happyNum;

        bool isHappy = testHappiness(happyNum);

        Case happyPair = {caseNum, happyNum, isHappy};
        happyNums.push_back(happyPair);
    }

    for (Case c : happyNums)
    {
        cout << c.caseNum << " " << c.happyNum << " ";
        if (c.isHappy)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}


bool 
testHappiness(int happyNum)
{
    if (!isPrime(happyNum))
        return false;
    
    while (happyNum >= 7)
    {
        happyNum = happySum(happyNum);
    }

    return happyNum == 1;
}

int
happySum(int k)
{
    int sum = 0;
    while (k > 0)
    {
        int digit = k % 10;
        sum += digit * digit;
        k /= 10;
    }

    return sum;
}

bool
isPrime(int k)
{
    if (k <= 1)
        return false;
    
    for (int i = 2; i <= sqrt(k); ++i)
    {
        if (k % i == 0)
            return false;
    }

    return true;
}