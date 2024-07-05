from problems.easy.valid_parentheses import Solution

solution = Solution()


def test_sample_one():
    s = "()"
    assert solution.isValid(s)


def test_sample_two():
    s = "()[]{}"
    assert solution.isValid(s)


def test_sample_three():
    s = "(]"
    assert not solution.isValid(s)


def test_sample_four():
    s = "([)]"
    assert not solution.isValid(s)


def test_sample_five():
    s = "{[]}"
    assert solution.isValid(s)


def test_sample_six():
    s = ""
    assert solution.isValid(s)


def test_sample_seven():
    s = "]([])"
    assert not solution.isValid(s)
