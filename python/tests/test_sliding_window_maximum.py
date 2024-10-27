from problems.hard.sliding_window_maximum import Solution

solution = Solution()


def test_sample_one():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    assert solution.maxSlidingWindow(nums, k) == [3, 3, 5, 5, 6, 7]


def test_sample_two():
    nums = [1]
    k = 1
    assert solution.maxSlidingWindow(nums, k) == [1]
