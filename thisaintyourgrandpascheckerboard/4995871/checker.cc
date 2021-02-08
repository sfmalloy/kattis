#include <iostream>
#include <string>
#include <vector>

int countRow(char p, std::string v);

int countCol(char p, int col, std::vector<std::string> v);

int main() {
    int N;
    std::cin >> N;

    std::vector<std::string> board(N);
    for (auto& r : board) {
        std::cin >> r;
    }
    
    bool valid = true;
    for (int i = 0; valid && i < N; ++i) {
        if (countRow('W', board[i]) != countRow('B', board[i]))
            valid = false;
        if (countCol('W', i, board) != countCol('B', i, board))
            valid = false;
        int count = 0;
        char prev = '.';
        for (char c : board[i]) {
            if (count == 3) {
                valid = false;
                break;
            }

            if (c == prev)
                count += 1;
            else {
                count = 1;
                prev = c;
            }
        }
        
        count = 0;
        prev = '.';
        for (int j = 0; j < N; ++j) {
            if (count == 3) {
                valid = false;
                break;
            }

            if (board[j][i] == prev)
                count += 1;
            else {
                count = 1;
                prev = board[j][i];
            }

        }

    }

    std::cout << valid << '\n';
    
    return 0;
}

int countRow(char p, std::string v) {
    int count = 0;
    for (char c : v) {
        if (c == p)
            count += 1;
    }

    return count;
}

int countCol(char p, int col, std::vector<std::string> v) {
    int count = 0;
    for (size_t i = 0; i < v.size(); ++i) {
        if (v[i][col] == p)
            count += 1;
    }

    return count;
}
