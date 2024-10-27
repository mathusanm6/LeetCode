from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        ans = 0
        while left < right:
            ans = max(ans, min(height[right], height[left]) * (right - left))
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return ans
