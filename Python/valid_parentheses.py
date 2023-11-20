from collections import deque


class Solution(object):
    def isOpenBracket(self, c):
        open_ = "([{"
        return c in open_

    def correspondingBracket(self, c):
        close = ")]}"
        open_ = "([{"
        for i in range(len(close)):
            if close[i] == c:
                return open_[i]
        return None

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dq = deque()
        for c in s:
            if self.isOpenBracket(self, c):
                dq.append(c)
            else:
                if len(dq) > 0 and self.correspondingBracket(self, c) == dq[-1]:
                    dq.pop()
                else:
                    return False
        return len(dq) == 0
