from problems.medium.permutation_in_string import Solution

solution = Solution()


def test_sample_one():
    s1 = "ab"
    s2 = "eidbaooo"
    assert solution.checkInclusion(s1, s2)


def test_sample_two():
    s1 = "ab"
    s2 = "eidboaoo"
    assert not solution.checkInclusion(s1, s2)


def test_sample_three():
    s1 = "a"
    s2 = "ab"
    assert solution.checkInclusion(s1, s2)
