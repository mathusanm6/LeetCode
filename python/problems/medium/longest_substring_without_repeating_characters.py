import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count_map = collections.defaultdict(int)
        max_length = 0

        for r, c in enumerate(s):
            count_map[c] += 1
            while count_map[c] > 1:
                count_map[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)

        return max_length
