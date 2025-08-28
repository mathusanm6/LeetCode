#include "two_sum.h"

#include <unordered_map>
#include <vector>

using std::unordered_map;
using std::vector;

vector<int> twoSum(const vector<int> &nums, const int target) {
  const int n = static_cast<int>(nums.size());
  unordered_map<int, int> index_of;
  index_of.reserve(nums.size()); // Reserve space to avoid rehashing
  for (int idx = 0; idx < n; ++idx) {
    const int num = nums[idx];
    int need = target - num;
    if (auto it = index_of.find(need); it != index_of.end()) {
      return {it->second, idx};
    }
    index_of.emplace(num, idx); // Note: no overwrite if x already exists
  }
  return {-1, -1}; // If no solution is found
}
