#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::string;
using std::pair;
using std::make_pair;
using std::swap;

long
gcd(long a, long b);

void
printFraction(pair<long, long> f);

int
main(int argc, char* argv[])
{
    size_t k;
    cin >> k;

    vector<pair<long, long>> answers(k);

    for (size_t i = 0; i < k; ++i)
    {
        pair<long, long> f1, f2;
        char op;
        cin >> f1.first >> f1.second >> op >> f2.first >> f2.second;

        long n = 0;
        long d = 0;

        if (op == '+' || op == '-')
        {
            if (f1.second != f2.second)
            {
                d = f1.second * f2.second;
                f1.first *= f2.second;
                f2.first *= f1.second;
            }
            else
            {
                d = f1.second;
            }

            n = op == '+' ? f1.first + f2.first : f1.first - f2.first;
        }
        else
        {
            if (op == '/')
            {
                swap(f2.first, f2.second);
            }

            n = f1.first * f2.first;
            d = f1.second * f2.second;
        }

        long factor = gcd(n, d);
        if (factor != 1)
        {
            n /= factor;
            d /= factor;
        }

        if (d < 0)
        {
            n *= -1;
            d *= -1;
        }

        answers[i] = make_pair(n, d);
    }

    for (const auto& f : answers)
    {
        printFraction(f);
    }
}

long
gcd(long a, long b)
{
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

void
printFraction(pair<long, long> f)
{
    cout << f.first << " / " << f.second << endl;
}