#include <iostream>
#include <vector>
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::string;

int
dayOfYear(vector<int>::iterator begin, vector<int>::iterator end, int day);

int
main(int argc, char* argv[])
{
    vector<int> monthDays { 31,28,31,30,31,30,31,31,30,31,30,31 };
    vector<string> days {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

    int day, month;
    std::cin >> day >> month;
    
    day = dayOfYear(monthDays.begin(), monthDays.begin() + (month - 1), day);
    int dayOfWeek = (day % 7) + 4;

    if (dayOfWeek > 7)
    {
        dayOfWeek -= 7;
    }

    cout << days[dayOfWeek - 1] << endl;

    return 0;
}

int
dayOfYear(vector<int>::iterator begin, vector<int>::iterator end, int day)
{
    int sum = 0;
    for (auto i = begin; i < end; ++i)
    {
        sum += *i;
    }

    return sum + day;
}