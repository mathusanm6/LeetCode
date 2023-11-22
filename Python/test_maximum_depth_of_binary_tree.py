from maximum_depth_of_binary_tree import Solution
from maximum_depth_of_binary_tree import TreeNode

def test_maximum_depth_of_binary_tree():
    solution = Solution

    # Testcase 1
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert solution.maxDepth(solution, root) == 3

    # Testcase 2
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert solution.maxDepth(solution, root) == 2

    # Testcase 3
    root = None
    assert solution.maxDepth(solution, root) == 0

    # Testcase 4
    root = TreeNode(0)
    assert solution.maxDepth(solution, root) == 1

    # Testcase 5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.left.left = TreeNode(5)
    assert solution.maxDepth(solution, root) == 5