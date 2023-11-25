# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.prev = float("inf")
        self.ans = float("inf")

    def inOrder(self, node):
        if node.left:
            self.inOrder(node.left)

        self.ans = min(self.ans, abs(node.val - self.prev))
        self.prev = node.val

        if node.right:
            self.inOrder(node.right)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inOrder(root)
        return self.ans
