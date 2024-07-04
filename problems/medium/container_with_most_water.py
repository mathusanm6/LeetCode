from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        ans = 0
        while l < r:
            ans = max(ans, min(height[r], height[l]) * (r - l))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return ans
