#include <iostream>
#include <vector>
#include <string>

const int SQUASH_SIZE = 5;

int check_space(const std::string& s);

int main() {
  int R, C;
  std::cin >> R >> C;

  std::vector<std::string> lines(R);
  for (int r = 0; r < R; ++r)
    std::cin >> lines[r];

  int squash[SQUASH_SIZE] = {0, 0, 0, 0, 0};
  for (int r = 0; r < R - 1; ++r) {
    for (int c = 0; c < C - 1; ++c) {
      std::string space_string = lines[r].substr(c, 2) + lines[r + 1].substr(c, 2);
      int car_count = check_space(space_string);
      if (car_count >= 0)
        ++squash[car_count];
    }
  }

  for (int i = 0; i < SQUASH_SIZE; ++i) {
    std::cout << squash[i] << '\n';
  }

  return 0;
}

// Return number of cars in 2x2 space.
// If building present, return -1
int check_space(const std::string& s) {
  
  int car_count = 0;
  for (const auto& c : s) {
    if (c == '#')
      return -1;
    else if (c == 'X')
      ++car_count;
  }

  return car_count;
}
