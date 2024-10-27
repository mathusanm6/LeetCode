from problems.easy.contains_duplicate import Solution

solution = Solution()


def test_one_duplicate():
    sample = [1, 2, 3, 1]
    assert solution.containsDuplicate(sample)


def test_no_duplicates():
    sample = [1, 2, 3, 4]
    assert not solution.containsDuplicate(sample)


def test_empty_array():
    sample = []
    assert not solution.containsDuplicate(sample)
