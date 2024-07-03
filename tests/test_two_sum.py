from problems.easy.two_sum import Solution

solution = Solution()


def test_sample_one():
    nums = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(nums, target) == [0, 1]


def test_sample_two():
    nums = [3, 2, 4]
    target = 6
    assert solution.twoSum(nums, target) == [1, 2]


def test_sample_three():
    nums = [3, 3]
    target = 6
    assert solution.twoSum(nums, target) == [0, 1]

def test_sample_four():
    nums = [-3, 1, 2, 3]
    target = 0
    assert solution.twoSum(nums, target) == [0, 3]
