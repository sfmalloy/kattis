#include <iostream>
#include <string>
#include <cstdio>

int main() {
  int N;
  std::cin >> N;

  std::string drink;
  std::cin >> drink;
  for (int i = N; i > 1; --i) {
    printf("%d bottles of %s on the wall, %d bottles of %s.\n", i, drink.c_str(), i, drink.c_str());
    printf("Take one down, pass it around, %d bottle%s of %s on the wall.\n\n", i-1, (i > 2 ? "s" : "") ,drink.c_str());
  }

  printf("1 bottle of %s on the wall, 1 bottle of %s.\n", drink.c_str(), drink.c_str());
  printf("Take it down, pass it around, no more bottles of %s.\n", drink.c_str());
  
  return 0;
}