#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>
 
int main() {
    long caseNum = 1;
    std::vector<std::vector<long>> cases;

    while (!std::cin.eof()) {
        // Get n numbers
        size_t n;
        std::cin >> n;
        std::vector<long> sumInts(n);
        std::for_each(sumInts.begin(), sumInts.end(), [](long& i){ std::cin >> i; });
 
        // Get m numbers
        size_t m;
        std::cin >> m;
        std::vector<long> queries;
        for (size_t i = 0; i < m; ++i) {
            long curr;
            std::cin >> curr;
            queries.push_back(curr);
        }

        std::vector<long> minSums;
        for (const long& q : queries) {
            long minSum = std::numeric_limits<long>::max();

            for (size_t i = 0; i < n - 1; ++i) {
                for (size_t j = i + 1; j < n; ++j) {
                    long currSum = sumInts[i] + sumInts[j];
                    if (minSum == std::numeric_limits<long>::max() || abs(currSum - q) < abs(minSum - q)) {
                        minSum = currSum;
                    }
                }
            }

            minSums.push_back(minSum);
        }

        std::vector<long> currCase;
        currCase.push_back(caseNum);
        for (size_t i = 0; i < m; ++i) {
            currCase.push_back(queries[i]);
            currCase.push_back(minSums[i]);
        }
        cases.push_back(currCase);

        ++caseNum;
    }

    cases.pop_back();
    // print output here
    for (const auto& c : cases) {
        for (size_t i = 0; i < c.size(); ++i) {
            if (i == 0)
                std::cout << "Case " << c[i] << ":\n";
            else {
                std::cout << "Closest sum to " << c[i] << " is " << c[i + 1] << ".\n";
                ++i;
            }
        }
    }
 
    return 0;
}