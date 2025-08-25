from problems.hard.minimum_window_substring import Solution

solution = Solution()


def test_sample_one():
    s = "ADOBECODEBANC"
    t = "ABC"
    assert solution.minWindow(s, t) == "BANC"


def test_sample_two():
    s = "a"
    t = "a"
    assert solution.minWindow(s, t) == "a"


def test_sample_three():
    s = "a"
    t = "aa"
    assert solution.minWindow(s, t) == ""
