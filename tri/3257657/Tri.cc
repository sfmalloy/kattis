#include <iostream>

using std::cout;
using std::cin;
using std::endl;

char
checkOperator(const int& a, const int& b, const int& c, bool& last);

int
doOperator(char op, int x, int y);

int
main(int argc, char* argv[])
{
    int a, b, c;
    cin >> a >> b >> c;

    bool last = true;

    char op = checkOperator(a, b, c, last);

    if (last)
    {
        cout << a << op << b << "=" << c << endl;
    }
    else
    {
        cout << a << "=" << b << op << c << endl;
    }
 
    return 0;
}

// First is automatically true
char
checkOperator(const int& a, const int& b, const int& c, bool& last)
{
    char ops[] { '+', '-', '*', '/' };

    for (char currOp : ops)
    {
        if (doOperator(currOp, a, b) == c)
        {
            return currOp;
        }
        else if (doOperator(currOp, b, c) == a)
        {
            last = false;
            return currOp;
        }
    }

    return '.';
}

int
doOperator(char op, int x, int y)
{
    if (op == '+')
        return x + y;
    else if (op == '-')
        return x - y;
    else if (op == '*')
        return x * y;
    else
        return x / y;
}