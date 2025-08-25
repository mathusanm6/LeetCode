class Solution(object):
    def isValid(self, s: str) -> bool:
        def isOpenBracket(c):
            open_ = "([{"
            return c in open_

        def correspondingBracket(c):
            close = ")]}"
            open_ = "([{"
            for i in range(len(close)):
                if close[i] == c:
                    return open_[i]
            return None

        stack = []
        for c in s:
            if isOpenBracket(c):
                stack.append(c)
            else:
                if len(stack) > 0 and correspondingBracket(c) == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
