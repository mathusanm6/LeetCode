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
        l, r = 0, 1
        min_len = float("inf")
        sub_sum = nums[0]
        while r <= n:
            if sub_sum < target:
                if r < n:
                    sub_sum += nums[r]
                r += 1
            else:
                diff = r - l
                if diff < min_len:
                    min_len = min(diff, min_len)
                sub_sum -= nums[l]
                l += 1
        return 0 if min_len == float("inf") else min_len
