class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def getIndex(c):
            return ord(c) - ord("A")

        count = [0] * 26
        left = 0
        ans = 0
        for right in range(len(s)):
            count[getIndex(s[right])] += 1
            while (right - left + 1) - max(count) > k:
                count[getIndex(s[left])] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
