from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        leftMax = height[0]  # O(1) space
        rightMax = height[n - 1]

        left = 1
        right = n - 2

        trapped_water = 0

        while left <= right:
            if leftMax < rightMax:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    trapped_water += leftMax - height[left]
                left += 1
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    trapped_water += rightMax - height[right]
                right -= 1

        return trapped_water
