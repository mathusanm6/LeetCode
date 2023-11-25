from problems.easy.merge_sorted_array import Solution

def test_merge_sorted_array():

    solution = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(nums1, 3, [2, 5, 6], 3)

    assert nums1 == [1, 2, 2, 3, 5, 6]

    # Test Case 2
    nums1 = [1]
    solution.merge(nums1, 1, [], 0)

    assert nums1 == [1]

    # Test Case 3
    nums1 = [0]
    solution.merge(nums1, 0, [1], 1)

    assert nums1 == [1]

    # Test Case 4
    nums1 = [1, 0]
    solution.merge(nums1, 1, [2], 1)

    assert nums1 == [1, 2]