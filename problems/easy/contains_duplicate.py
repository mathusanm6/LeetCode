from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for val in nums:
            if val in seen:  # Duplicate value found
                return True
            seen.add(val)
        return False
