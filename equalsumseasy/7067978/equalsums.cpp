#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>

bool getSums(std::unordered_map<int, std::vector<int>>& sums, std::vector<int> addends,
            const std::vector<int>& nums, int currSum, int startIdx, int currDepth, int maxDepth)
{
    if (currDepth == maxDepth)
    {
        if (sums.find(currSum) != sums.end())
        {
            for (int x : addends)
                std::cout << x << ' ';
            std::cout << '\n';
            for (int x : sums[currSum])
                std::cout << x << ' ';
            std::cout << '\n';
            return true;
        }
        
        sums[currSum] = std::vector<int>(addends.begin(), addends.end());
        return false;
    }
    for (int i = startIdx; i < nums.size() - maxDepth; ++i)
    {
        addends.push_back(nums[i]);
        bool found = getSums(sums, addends, nums, currSum + nums[i], i + 1, currDepth + 1, maxDepth);
        if (found)
            return true;
        else
            addends.pop_back();
    }
    return false;
}

int main()
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        int N;
        std::cin >> N;

        std::vector<int> nums(N);
        for (int i = 0; i < N; ++i)
            std::cin >> nums[i];
        
        std::cout << "Case #" << t << ":\n";
        std::unordered_map<int, std::vector<int>> sums;
        std::vector<int> addends;
        bool found = false;
        for (int d = 1; d < N; ++d)
        {
            found = getSums(sums, addends, nums, 0, 0, 0, d);
            if (found)
                break;
        }
    }
    return 0;
}