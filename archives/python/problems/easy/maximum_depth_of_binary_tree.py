# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left = 0
        if root.left:
            left += self.maxDepth(self, root.left)
        right = 0
        if root.right:
            right += self.maxDepth(self, root.right)
        return 1 + max(left, right)
