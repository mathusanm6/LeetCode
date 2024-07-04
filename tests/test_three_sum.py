from problems.medium.three_sum import Solution


solution = Solution()


def test_sample_one():
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert solution.threeSum(nums) == expected


def test_sample_two():
    nums = [0, 1, 1]
    expected = []
    assert solution.threeSum(nums) == expected


def test_sample_three():
    nums = [0, 0, 0]
    expected = [[0, 0, 0]]
    assert solution.threeSum(nums) == expected


def test_sample_four():
    nums = [0, 0, 0, 0]
    expected = [[0, 0, 0]]
    assert solution.threeSum(nums) == expected
