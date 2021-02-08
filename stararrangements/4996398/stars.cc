#include <iostream>

bool arrange(int s, int k, bool alt);

int main() {
    int s;
    std::cin >> s;
    std::cout << s << ":\n";
    for (int i = 2; i <= (s / 2) + 1; ++i) {
        if (arrange(s, i, true))
            std::cout << i << ',' << (i - 1) << std::endl;
        if (arrange(s, i, false))
            std::cout << i << ',' << i << std::endl;
    }

    return 0;
}

bool arrange(int s, int k, bool alt) {
    int sum = 0;
    for (int i = 0; sum < s; ++i) {
        if (alt && i % 2 == 1)
            sum += k - 1;
        else
            sum += k;
    }

    return sum == s;
}
