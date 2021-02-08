#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

int main() {
    std::string a, b;
    std::cin >> a >> b;
   
    int size = std::max(a.size(), b.size());
    std::vector<int> result(size + 1);
    int carry = 0;
    for (auto i = result.rbegin(); i != result.rend(); ++i) {
        int curr_result = carry;

        if (a.size() > 0) {
            curr_result += a.back() - 48;
            a.pop_back();
        } 
        
        if (b.size() > 0) {
            curr_result += b.back() - 48;
            b.pop_back();
        }

        if (curr_result > 9) {
            carry = 1;
            curr_result -= 10;
        } else {
            carry = 0;
        }
         
        *i = curr_result;
    }

    if (result[0] > 0)
        std::cout << result[0];
    for (size_t i = 1; i < result.size(); ++i) {
        std::cout << result[i];
    }

    std::cout << std::endl;
    return 0;
}
