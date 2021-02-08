#include <iostream>
#include <vector>
#include <map>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::map;
using std::pair;

void
inputTimes(vector<int>& times);

void
getDifferences(const int& exitTime, map<int, int>& differences, vector<int>& entryTimes);

int
main(int argc, char* argv[])
{
    int N, M;
    cin >> N >> M;
    vector<int> entryTimes(N), exitTimes(M);

    inputTimes(entryTimes);
    inputTimes(exitTimes);

    map<int, int> differences;

    for (auto i = exitTimes.begin(); i != exitTimes.end(); ++i)
    {
        getDifferences(*i, differences, entryTimes);
    }

    int maxDifference = 0;
    int maxOccurance = 0;

    for (auto& t : differences)
    {
        if (t.first > maxDifference && t.second > maxOccurance)
        {
            maxDifference = t.first;
            maxOccurance = t.second;
        }    
    }

    cout << maxDifference << endl;

    return 0;
}

void
inputTimes(vector<int>& times)
{
    for (auto i = times.begin(); i != times.end(); ++i)
    {
        int t;
        cin >> t;
        *i = t;
    }
}

void
getDifferences(const int& exitTime, map<int, int>& differences, vector<int>& entryTimes)
{
    for (size_t i = 0; i < entryTimes.size() && entryTimes[i] < exitTime; ++i)
    {
        differences[exitTime - entryTimes[i]] += 1;
    }
}