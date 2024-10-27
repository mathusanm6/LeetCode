from problems.easy.summary_ranges import Solution


def test_summary_ranges():
    solution = Solution

    # Test Case 1
    nums = [0, 1, 2, 4, 5, 7]
    assert solution.summaryRanges(solution, nums) == ["0->2", "4->5", "7"]

    # Test Case 2
    nums = [0, 2, 3, 4, 6, 8, 9]
    assert solution.summaryRanges(solution, nums) == ["0", "2->4", "6", "8->9"]

    # Test Case 3
    nums = []
    assert solution.summaryRanges(solution, nums) == []

    # Test Case 4
    nums = [-1]
    assert solution.summaryRanges(solution, nums) == ["-1"]

    # Test Case 5
    nums = [-100, 0, 1, 2, 100]
    assert solution.summaryRanges(solution, nums) == ["-100", "0->2", "100"]
