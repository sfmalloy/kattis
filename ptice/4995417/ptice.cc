#include <iostream>
#include <string>
#include <algorithm>

int main() {
    int N;
    std::cin >> N;
    
    std::string adrian = "ABC", bruno = "BABC", goran = "CCAABB", answers;
    int a_count = 0, b_count = 0, g_count = 0;
    std::cin >> answers;
    for (int i = 0; i < N; ++i) {
        char a = adrian[i % adrian.size()], b = bruno[i % bruno.size()], g = goran[i % goran.size()];

        if (a == answers[i])
            ++a_count;
        if (b == answers[i])
            ++b_count;
        if (g == answers[i])
            ++g_count;
    }

    int m = std::max(a_count, std::max(b_count, g_count));
    std::cout << m << '\n';
    if (a_count == m)
        std::cout << "Adrian" << '\n';
    if (b_count == m)
        std::cout << "Bruno" << '\n';
    if (g_count == m)
        std::cout << "Goran" << '\n';
    return 0;
}
