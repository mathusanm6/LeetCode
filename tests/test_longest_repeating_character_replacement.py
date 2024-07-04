from problems.medium.longest_repeating_character_replacement import Solution

solution = Solution()


def test_sample_one():
    s = "ABAB"
    k = 2
    assert solution.characterReplacement(s, k) == 4


def test_sample_two():
    s = "AABABBA"
    k = 1
    assert solution.characterReplacement(s, k) == 4
