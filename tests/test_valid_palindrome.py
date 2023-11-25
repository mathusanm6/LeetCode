from problems.easy.valid_palindrome import Solution


def test_is_palindrome():
    solution = Solution()

    # Test Case 1
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True

    # Test Case 2
    assert solution.isPalindrome("") == True

    # Test Case 3
    assert solution.isPalindrome("a") == True

    # Test Case 4
    assert solution.isPalindrome("race a car") == False

    # Test Case 5
    assert solution.isPalindrome("Aa") == True
