from problems.medium.longest_consecutive_sequence import Solution

solution = Solution()


def test_sample_one():
    nums = [100, 4, 200, 1, 3, 2]
    assert solution.longestConsecutive(nums) == 4


def test_sample_two():
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    assert solution.longestConsecutive(nums) == 9
