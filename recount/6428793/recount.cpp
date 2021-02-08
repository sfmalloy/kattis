#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>

int main() {
  std::string name;
  std::unordered_map<std::string, int> votes;
  while (std::getline(std::cin, name)) {
    if (name == "***")
      break;
    votes[name] += 1;
  }

  auto max = std::max_element(std::begin(votes), std::end(votes), [&](const auto& a, const auto& b) {
    return a.second < b.second;
  });

  int maxCount = 0;
  for (auto& p : votes) {
    if (p.second == max->second) {
      maxCount += 1;
      if (maxCount > 1)
        break;
    }
  }
  
  if (maxCount > 1) {
    std::cout << "Runoff!" << '\n';    
  } else {
    std::cout << max->first << '\n';
  }

  return 0;
}