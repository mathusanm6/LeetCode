from problems.easy.minimum_absolute_difference_in_bst import Solution, TreeNode


def test_get_minimum_difference():
    # Test case 1
    solution = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    assert solution.getMinimumDifference(root) == 1

    # Test case 2
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)

    assert solution.getMinimumDifference(root) == 1

    # Test case 3
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(5)
    root.right.left = TreeNode(3)

    assert solution.getMinimumDifference(root) == 2

    # Test case 4
    solution = Solution()
    root = TreeNode(543)
    root.left = TreeNode(384)
    root.right = TreeNode(652)
    root.left.right = TreeNode(445)
    root.right.right = TreeNode(699)

    assert solution.getMinimumDifference(root) == 47

    # Test case 5
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)

    assert solution.getMinimumDifference(root) == 1
