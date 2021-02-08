#include <iostream>
#include <vector>
#include <algorithm>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::sort;
using std::abs;

int
main(int argc, char* argv[])
{
    size_t S, C;
    int K;
    cin >> S >> C >> K;
    vector<int> socks;

    for (size_t i = 0; i < S; ++i)
    {
        int tempSock;
        cin >> tempSock;
        socks.push_back(tempSock);
    }

    sort(socks.begin(), socks.end());

    vector<vector<int>> machines;

    while (socks.size() > 0)
    {
        vector<int> currMachine;
        int biggestSock = socks[socks.size() - 1];
        currMachine.push_back(biggestSock);
        socks.pop_back();

        while (socks.size() > 0 && currMachine.size() < C)
        {
            int currSock = socks[socks.size() - 1];
            if (biggestSock - currSock <= K)
                currMachine.push_back(currSock);
            else
                break;
            
            socks.pop_back();
        }

        machines.push_back(currMachine);
    }

    cout << machines.size() << endl;

    return 0;
}