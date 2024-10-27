from problems.medium.generate_parentheses import Solution

solution = Solution()


def test_sample_one():
    n = 3
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert solution.generateParenthesis(n) == expected


def test_sample_two():
    n = 1
    expected = ["()"]
    assert solution.generateParenthesis(n) == expected
