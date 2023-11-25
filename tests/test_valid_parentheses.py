from problems.easy.valid_parentheses import Solution


def test_valid_parentheses():
    solution = Solution

    # Test Case 1
    s = "()"
    assert solution.isValid(solution, s) is True

    # Test Case 2
    s = "()[]{}"
    assert solution.isValid(solution, s) is True

    # Test Case 3
    s = "(]"
    assert solution.isValid(solution, s) is False

    # Test Case 4
    s = "([)]"
    assert solution.isValid(solution, s) is False

    # Test Case 5
    s = "{[]}"
    assert solution.isValid(solution, s) is True

    # Test Case 6
    s = ""
    assert solution.isValid(solution, s) is True

    # Test Case 7
    s = "]([])"
    assert solution.isValid(solution, s) is False
