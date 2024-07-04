from problems.medium.container_with_most_water import Solution

solution = Solution()


def test_sample_one():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert solution.maxArea(height) == 49


def test_sample_two():
    height = [1, 1]
    assert solution.maxArea(height) == 1
