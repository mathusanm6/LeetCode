from problems.medium.longest_substring_without_repeating_characters import Solution

solution = Solution()


def test_sample_one():
    s = "abcabcbb"
    assert solution.lengthOfLongestSubstring(s) == 3


def test_sample_two():
    s = "bbbbb"
    assert solution.lengthOfLongestSubstring(s) == 1


def test_sample_three():
    s = "pwwkew"
    assert solution.lengthOfLongestSubstring(s) == 3
