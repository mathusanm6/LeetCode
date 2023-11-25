from problems.easy.valid_palindrome import Solution


def test_is_palindrome():
    solution = Solution()

    # Test Case 1
    assert solution.isPalindrome("A man, a plan, a canal: Panama")

    # Test Case 2
    assert solution.isPalindrome("")

    # Test Case 3
    assert solution.isPalindrome("a")

    # Test Case 4
    assert not solution.isPalindrome("race a car")

    # Test Case 5
    assert solution.isPalindrome("Aa")
