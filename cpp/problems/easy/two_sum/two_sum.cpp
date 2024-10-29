#include "two_sum.h"

vector<int> twoSum(vector<int> &nums, int target)
{
    unordered_map<int, int> map;

    for (size_t i = 0; i < nums.size(); ++i)
    {
        int complement = target - nums[i];
        if (map.find(complement) != map.end())
        {
            return {map[complement], static_cast<int>(i)};
        }
        else
        {
            map[nums[i]] = static_cast<int>(i);
        }
    }

    return {};
}