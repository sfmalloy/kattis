#include <iostream>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <tuple>

int main() {
    int cases;
    std::cin >> cases;

    std::vector<std::pair<int, int>> dims;

    for (int i = 0; i < cases; ++i) {
        int x, y;
        std::cin >> x >> y;
        dims.push_back(std::make_pair(x, y));
    }

    for (int i = 0; i < cases; ++i) {
        int x = dims[i].first, y = dims[i].second;

        // Constant
        int k = (4 * x) + (4 * y);

        // Depends on x and y, both pos and neg solutions
        double h1 = (k + sqrt((k * k) - (48 * x * y))) / 24.0;
        double h2 = (k - sqrt((k * k) - (48 * x * y))) / 24.0;

        double a1 = x - (2 * h1);
        double b1 = y - (2 * h1);

        double a2 = x - (2 * h2);
        double b2 = y - (2 * h2);

        double volume1 = a1 * b1 * h1;
        double volume2 = a2 * b2 * h2;

        printf("%.11f\n", (volume1 > volume2 ? volume1 : volume2));
    }

    return 0;
}
