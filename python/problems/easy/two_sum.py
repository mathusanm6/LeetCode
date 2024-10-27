from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        complement_map = {}
        for i in range(n):
            val = nums[i]
            if val in complement_map:
                return [complement_map[val], i]
            complement_map[target - val] = i
        return [-1, -1]  # This case isn't expected
