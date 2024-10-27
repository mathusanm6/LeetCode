import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        freq_s1 = collections.Counter(s1)
        freq_s2 = collections.Counter(s2[: len(s1)])

        if freq_s1 == freq_s2:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            freq_s2[s2[left]] -= 1
            freq_s2[s2[right]] += 1
            if freq_s1 == freq_s2:
                return True
            left += 1

        return False
