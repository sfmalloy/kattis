#include <iostream>
#include <map>
#include <set>
#include <vector>

int main() {
    int n, c;
    std::cin >> n >> c;
    
    std::map<int, int> freq;
    std::vector<int> occur_order;
    int t;
    for (int i = 0; i < n; ++i) {
        std::cin >> t;
        freq[t] += 1;
        if (freq[t] == 1)
            occur_order.push_back(t);
    }

    std::map<int, std::vector<int>> sorted;
    for (auto it = occur_order.begin(); it != occur_order.end(); ++it) {
        sorted[freq[*it]].push_back(*it);
    }

    for (auto it = sorted.rbegin(); it != sorted.rend(); ++it) {
        for (int x : it->second) {
            for (int i = 0; i < it->first; ++i) {
                std::cout << x << ' ';   
            }
        }
    }

    std::cout << std::endl;

    return 0;   
}
