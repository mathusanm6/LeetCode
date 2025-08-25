class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        n = len(nums)
        left, right = 0, 1
        min_len = float("inf")
        sub_sum = nums[0]
        while right <= n:
            if sub_sum < target:
                if right < n:
                    sub_sum += nums[right]
                right += 1
            else:
                diff = right - left
                if diff < min_len:
                    min_len = min(diff, min_len)
                sub_sum -= nums[left]
                left += 1
        return 0 if min_len == float("inf") else min_len
