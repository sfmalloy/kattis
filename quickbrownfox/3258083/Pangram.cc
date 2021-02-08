#include <iostream>
#include <ctype.h>
#include <string>
#include <algorithm>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::tolower;
using std::string;
using std::find;
using std::vector;

int
main(int argc, char* argv[])
{
    size_t cases;
    cin >> cases;

    vector<string> alphabets;

    for(size_t i = 0; i <= cases; ++i)
    {
        string sentence;
        getline(cin, sentence);
        
        string alphabet = "abcdefghijklmnopqrstuvwxyz";
        
        for (char c : sentence)
        {
            string::iterator a = find(alphabet.begin(), alphabet.end(), tolower(c));
            if (a != alphabet.end())
            {
                alphabet.erase(a, a + 1);
            }
        }

        alphabets.push_back(alphabet);
    }

    vector<string> finalAlphabets(alphabets.begin() + 1, alphabets.end());

    for (string a : finalAlphabets)
    {
        if (a.size() > 0)
            cout << "missing " << a << endl;
        else
            cout << "pangram" << endl;
    }

    return 0;
}