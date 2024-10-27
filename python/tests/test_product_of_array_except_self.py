from problems.medium.product_of_array_except_self import Solution

solution = Solution()


def test_sample_one():
    nums = [1, 2, 3, 4]
    assert solution.productExceptSelf(nums) == [24, 12, 8, 6]


def test_sample_two():
    nums = [-1, 1, 0, -3, 3]
    assert solution.productExceptSelf(nums) == [0, 0, 9, 0, 0]
