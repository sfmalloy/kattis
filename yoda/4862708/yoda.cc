#include <iostream>
#include <vector>
#include <cmath>
#include <string>

std::vector<int> digitsToVector(int x);

int yodaNum(std::vector<int> x);

int main() {
    int n, m;
    std::cin >> n >> m;

    std::vector<int> a = digitsToVector(n), b = digitsToVector(m);
    for (auto i = a.rbegin(), j = b.rbegin(); i != a.rend() && j != b.rend(); ++i, ++j) {
        if (*i > *j) {
            *j = -1;
        } else if (*i < *j) {
            *i = -1;
        }
    }

    int aYoda = yodaNum(a), bYoda = yodaNum(b);
    std::cout << ((aYoda == -1) ? "YODA" : std::to_string(aYoda)) << '\n' << ((bYoda == -1) ? "YODA" : std::to_string(bYoda)) << '\n';
    return 0;
}

std::vector<int> digitsToVector(int x) {
    int numLen = ceil(log10(x));
    std::vector<int> v(numLen);
    for (auto i = v.rbegin(); i != v.rend(); ++i) {
        *i = x % 10;
        x /= 10;
    }

    return v;
}

int yodaNum(std::vector<int> x) {
    int s = 0, neg = 0, pow10 = 1;
    for (auto i = x.rbegin(); i != x.rend(); ++i) {
        if (*i >= 0) {
            s += *i * pow10;
            pow10 *= 10;
        } else {
            ++neg;
        }
    }

    return (neg == x.size()) ? -1 : s;
}
