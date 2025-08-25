from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        leftmost = [0] * n  # O(n) space
        rightmost = [0] * n

        for i in range(1, n):
            leftmost[i] = max(leftmost[i - 1], height[i - 1])
            rightmost[n - 1 - i] = max(rightmost[n - i], height[n - i])

        trapped_water = 0

        for i in range(n):
            trapped_water += max(0, min(leftmost[i], rightmost[i]) - height[i])

        return trapped_water
