#include <iostream>
#include <queue>

int main() {
  int s, t, n;
  std::cin >> s >> t >> n;

  std::queue<int> d;
  for (int i = 0; i < n + 1; ++i) {
    int curr;
    std::cin >> curr;
    d.push(curr);
  }

  int tick = s;
  int b, c;
  while (std::cin >> b >> c) {
    tick += d.front() + b + (c - (tick % c));
    d.pop();
  }

  std::cout << (tick <= t ? "yes" : "no") << '\n';

  return 0;
}
