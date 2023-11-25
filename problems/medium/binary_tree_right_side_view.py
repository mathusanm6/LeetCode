from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        dq = deque([root])
        while dq:
            rightMost = None
            n = len(dq)

            for i in range(n):
                node = dq.popleft()
                if node:
                    rightMost = node
                    dq.append(node.left)
                    dq.append(node.right)
            if rightMost:
                res.append(rightMost.val)
        return res
