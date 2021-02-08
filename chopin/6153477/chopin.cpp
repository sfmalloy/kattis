#include <iostream>
#include <sstream>
#include <string>

int
main()
{
  std::string line;
  int currCase = 1;
  while (std::getline(std::cin, line))
  {
    std::cout << "Case " << currCase++ << ": ";
    if (line[1] != ' ')
    {
      char note, acc;
      if (line[1] == 'b')
      {
        if (line[0] != 'A')
          note = line[0] - 1;
        else
          note = 'G';
        acc = '#';
      }
      else
      {
        if (line[0] != 'G')
          note = line[0] + 1;
        else
          note = 'A';
        acc = 'b';
      }

      std::cout << note << acc << ' ' << line.substr(line.find(' ') + 1) << '\n';
    }
    else
      std::cout << "UNIQUE" << '\n';
  }

  return 0;
}