class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums

        res = []

        start = nums[0]
        offset = 1
        for i in range(1, len(nums)):
            if start + offset == nums[i]:
                offset += 1
                continue
            else:
                if offset > 1:
                    res.append(str(start) + "->" + str(start + offset - 1))

                else:
                    res.append(str(start))

                start = nums[i]
                offset = 1
        if offset > 1:
            res.append(str(start) + "->" + str(start + offset - 1))
        else:
            res.append(str(start))
        return res
