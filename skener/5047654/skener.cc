#include <iostream>
#include <string>
#include <vector>

int main() {
    int r, c, zr, zc;
    std::cin >> r >> c >> zr >> zc;
    
    std::string line;
    for (int i = 0; i < r; ++i) {
        std::cin >> line;
        std::vector<std::string> enlarge(zr);
        for (int j = 0; j < c; ++j) {
            char ch = line[j];
            for (int k = 0; k < zr; ++k) {
                for (int l = 0; l < zc; ++l) {
                    enlarge[k].push_back(ch);
                }
            }
        }

        for (const std::string& s : enlarge) {
            std::cout << s << std::endl;
        }
    }

    return 0;
}
