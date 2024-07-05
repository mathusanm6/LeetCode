from problems.medium.evaluate_reverse_polish_notation import Solution

solution = Solution()


def test_sample_one():
    tokens = ["2", "1", "+", "3", "*"]
    assert solution.evalRPN(tokens) == 9


def test_sample_two():
    tokens = ["4", "13", "5", "/", "+"]
    assert solution.evalRPN(tokens) == 6


def test_sample_three():
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert solution.evalRPN(tokens) == 22
