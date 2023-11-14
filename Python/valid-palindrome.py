class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isAlnumChar(c):
            if ord('0') <= ord(c) <= ord('9'):
                return True
            if ord('a') <= ord(c) <= ord('z'):
                return True
            if ord('A') <= ord(c) <= ord('Z'):
                return True
            return False
        
        l, r = 0, len(s) - 1
        s = s.lower()

        while l < r:
            s_l, s_r = s[l], s[r]
            if not isAlnumChar(s_l):
                l += 1
                continue
            if not isAlnumChar(s_r):
                r -= 1
                continue
            
            if s_l != s_r:
                return False
            l += 1
            r -= 1
        return True