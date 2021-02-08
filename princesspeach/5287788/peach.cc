#include <iostream>
#include <set>

int main() {
  int max, n;
  std::cin >> max >> n;

  int x;
  std::set<int> got;
  while (std::cin >> x) {
    got.insert(x);
  }

  for (int i = 0; i < max; ++i) {
    if (got.find(i) == got.end())
      std::cout << i << '\n';
  }

  std::cout << "Mario got " << got.size() << " of the dangerous obstacles.\n";

  return 0;
}
