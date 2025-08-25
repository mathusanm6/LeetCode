class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isAlnumChar(c):
            if ord("0") <= ord(c) <= ord("9"):
                return True
            if ord("a") <= ord(c) <= ord("z"):
                return True
            if ord("A") <= ord(c) <= ord("Z"):
                return True
            return False

        left, right = 0, len(s) - 1
        s = s.lower()

        while left < right:
            s_l, s_r = s[left], s[right]
            if not isAlnumChar(s_l):
                left += 1
                continue
            if not isAlnumChar(s_r):
                right -= 1
                continue

            if s_l != s_r:
                return False
            left += 1
            right -= 1
        return True
