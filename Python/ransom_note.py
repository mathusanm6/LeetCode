class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        def index(c):
            return ord(c) - ord("a")

        count_l = [0] * 26
        for c in magazine:
            count_l[index(c)] += 1
        for c in ransomNote:
            idx_c = index(c)
            count_l[idx_c] -= 1
            if count_l[idx_c] < 0:
                return False
        return True
