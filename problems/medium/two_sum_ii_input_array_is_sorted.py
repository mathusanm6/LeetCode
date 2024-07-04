from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            tmp_sum = numbers[l] + numbers[r]
            if tmp_sum == target:
                return [l + 1, r + 1]
            elif tmp_sum < target:
                l += 1
            else:
                r -= 1
        return [-1, -1]
