#include <iostream>
#include <vector>

int main()
{
    std::string line;
    size_t longest = 0;
    std::vector<size_t> lengths;

    while (std::getline(std::cin, line))
    {
        longest = std::max(longest, line.size());
        lengths.push_back(line.size());
    }

    size_t penalty = 0;
    for (size_t i = 0; i < lengths.size() - 1; ++i)
    {
        if (lengths[i] < longest)
        {
            size_t diff = longest - lengths[i];
            penalty += diff * diff;
        }
    }

    std::cout << penalty << '\n';
    return 0;
}
