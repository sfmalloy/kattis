#include <iostream>
#include <vector>
#include <unordered_set>
#include <cmath>
#include <algorithm>

int
check_slopes(int r, int c, const std::vector<int>& taken_spots)
{
  for (int k = 0; k < taken_spots.size(); ++k)
    if (std::abs(r - k) == std::abs(c - taken_spots[k]))
      return false;
  return true;
}

int
valid_queens(int n, const std::vector<std::vector<bool>>& holes,
            std::vector<int>& taken_spots, int prev, int d, int valid)
{
  for (int i = 0; i < n; ++i)
  {
    if (!holes[d][i] && std::find(taken_spots.begin(), taken_spots.end(), i) == taken_spots.end())
    {
      if (prev == -1 || check_slopes(d, i, taken_spots))
      {
        if (d == n - 1)
          return valid + 1;
        taken_spots.push_back(i);
        valid = valid_queens(n, holes, taken_spots, i, d+1, valid);
        taken_spots.pop_back();
      }
    }
  }

  return valid;
}

int
main()
{
  while (true)
  {
    int n, m;
    std::cin >> n >> m;
    if (n == 0 && m == 0)
      break;

    std::vector<std::vector<bool>> holes(n, std::vector<bool>(n));
    int r, c;
    for (int h = 0; h < m; ++h)
    {
      std::cin >> r >> c;
      holes[r][c] = true;
    }

    std::vector<int> taken_spots;
    std::cout << valid_queens(n, holes, taken_spots, -1, 0, 0) << '\n';
  }

  return 0;
}
