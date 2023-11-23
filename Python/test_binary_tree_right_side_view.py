from binary_tree_right_side_view import Solution
from binary_tree_right_side_view import TreeNode


def test_right_side_view():
    solution = Solution

    # Testcase 1 (my own test case)
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(10)
    root.left.left.left = TreeNode(11)
    root.left.left.left.right = TreeNode(20)
    assert solution.rightSideView(solution, root) == [3, 9, 10, 11, 20]

    # Testcase 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    assert solution.rightSideView(solution, root) == [1, 3, 4]

    # Testcase 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    assert solution.rightSideView(solution, root) == [1, 3, 5]

    # Testcase 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(6)
    assert solution.rightSideView(solution, root) == [1, 3, 4, 6]
