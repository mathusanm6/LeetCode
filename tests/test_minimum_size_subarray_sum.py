from problems.medium.minimum_size_subarray_sum import Solution

def test_minimum_size_subarray_sum():

    solution = Solution()

    # Test Case 1
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2

    # Test Case 2
    assert solution.minSubArrayLen(4, [1, 4, 4]) == 1

    # Test Case 3
    assert solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0

    # Test Case 4
    assert solution.minSubArrayLen(11, [1, 2, 3, 4, 5]) == 3