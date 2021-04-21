#include <iostream>
#include <iomanip>

int main() {
    int N;
    std::cin >> N;

    float avg_x = 0;
    float avg_y = 0;
    for (int i = 0; i < N; ++i)
    {
        float x = 0;
        float y = 0;
        std::cin >> x >> y;
        avg_x += x;
        avg_y += y;
    }

    avg_x /= N;
    avg_y /= N;

    std::cout << std::fixed << std::setprecision(6) << avg_y - avg_x << '\n';

    return 0;
}