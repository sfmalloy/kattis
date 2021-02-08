#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

std::string rotate(std::string msg, int N) {
  std::reverse(msg.begin(), msg.end());

  for (size_t i = 0; i < msg.length(); i += N)
    std::reverse(msg.begin() + i, msg.begin() + i + N);

  std::string rotated = msg;
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j)
      rotated[i * N + j] = msg[j * N + i];

  return rotated;
}

int main() {
  int cases;
  std::cin >> cases;

  for (int i = 0; i < cases; ++i) {
    std::string original;
    std::cin >> original;
    
    int len = original.length();
    int N = std::sqrt(len);

    if (N * N < len)
      N += 1;

    for (int diff = (N * N) - len; diff > 0; --diff)
      original += '*';

    std::string rotated = rotate(original, N);
    
    for (char& c : rotated)
      if (c != '*')
        std::cout << c;
    std::cout << '\n';
  }

  return 0;
}
