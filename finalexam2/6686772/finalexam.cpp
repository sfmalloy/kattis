#include <iostream>

int
main()
{
  int N;
  std::cin >> N;

  int correct = 0;
  char curr, prev;
  std::cin >> prev;
  for (int i = 1; i < N; ++i) {
    std::cin >> curr;
    if (prev == curr)
      ++correct;
    prev = curr;
  }

  std::cout << correct << '\n';
  return 0;
}