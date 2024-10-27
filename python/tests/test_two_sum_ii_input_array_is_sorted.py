from problems.medium.two_sum_ii_input_array_is_sorted import Solution

solution = Solution()


def test_sample_one():
    numbers = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(numbers, target) == [1, 2]


def test_sample_two():
    numbers = [2, 3, 4]
    target = 6
    assert solution.twoSum(numbers, target) == [1, 3]


def test_sample_three():
    numbers = [-1, 0]
    target = -1
    assert solution.twoSum(numbers, target) == [1, 2]
