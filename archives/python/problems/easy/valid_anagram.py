import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        diff_map = collections.defaultdict(int)
        for c in s:
            diff_map[c] += 1
        for c in t:
            diff_map[c] -= 1
        for val in diff_map.values():
            if val != 0:
                return False
        return True
