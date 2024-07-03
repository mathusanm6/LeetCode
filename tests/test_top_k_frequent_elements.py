from problems.medium.top_k_frequent_elements import Solution

solution = Solution()


def test_sample_big():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    assert sorted(solution.topKFrequent(nums, k)) == [1, 2]


def test_sample_small():
    nums = [1]
    k = 1
    assert solution.topKFrequent(nums, k) == [1]


def test_sample_unsorted_big():
    nums = [1, 0, -12, 13, -12, 0, 3, 1]
    k = 3
    assert sorted(solution.topKFrequent(nums, k)) == [-12, 0, 1]
