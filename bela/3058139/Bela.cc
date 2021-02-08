#include <iostream>
#include <vector>
#include <tuple>
#include <string>
#include <algorithm>

using std::cout;
using std::cin;
using std::endl;

std::pair<char, int>
makeCard (char card, int score);

template <typename T>
int
indexOf (const std::vector<T>& v, T value);

int
main (int argc, char* argv[])
{
    std::vector<char> number { 'A', 'K', 'Q', 'J', 'T', '9', '8', '7' };
    std::vector<int> dominant { 11, 4, 3, 20, 10, 14, 0, 0 };
    std::vector<int> nondominant { 11, 4, 3, 2, 10, 0, 0, 0 };

    int N;
    char B;

    std::cin >> N >> B;

    int score = 0;

    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < 4; ++j) 
        {
            std::string tempCard;
            std::cin >> tempCard;

            char tempNumber = tempCard.at (0);

            if(tempCard.at (1) == B)
                score += dominant[indexOf (number, tempNumber)];
            else
                score += nondominant[indexOf (number, tempNumber)];
        }
    }

    std::cout << score << std::endl;

    return 0;
}

template <typename T>
int
indexOf (const std::vector<T>& v, T value)
{
    for (size_t i = 0; i < v.size (); ++i)
    {
        if (v[i] == value)
        {
            return i;
        }
    }

    return -1;
}