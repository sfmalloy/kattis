#include <iostream>
#include <string>

int
main()
{
  std::string line;
  int currCase = 1;
  while (std::getline(std::cin, line))
  {
    std::cout << "Case " << currCase++ << ": " << 
    (line[1] == ' ' ? "UNIQUE" : 
      (line[1] == 'b' ? 
        (line[0] != 'A' ? 
          std::string(1, (line[0] - 1)) : "G") + "# " :
        (line[0] != 'G' ? 
          std::string(1, (line[0] + 1)) : "A") + "b ") +
      line.substr(line.find(' ') + 1)) << '\n';
  }

  return 0;
}