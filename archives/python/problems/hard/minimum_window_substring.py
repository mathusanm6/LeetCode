import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq_t = collections.Counter(t)
        freq_window = collections.defaultdict(int)
        left = 0
        have = 0
        need = len(freq_t)
        ans = (float("inf"), 0, 0)

        for right in range(len(s)):
            c = s[right]
            if c in freq_t:
                freq_window[c] += 1
                if freq_window[c] == freq_t[c]:
                    have += 1

            while have == need:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                tmp = s[left]
                if tmp in freq_t:
                    freq_window[tmp] -= 1
                    if freq_window[tmp] < freq_t[tmp]:
                        have -= 1
                left += 1

        left, right = ans[1], ans[2]
        return s[left : right + 1] if ans[0] != float("inf") else ""
