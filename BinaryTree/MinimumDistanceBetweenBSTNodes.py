import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.prev_node = None
        self.min_value = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.visitRoot(root)

        return self.min_value

    def visitRoot(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.visitRoot(root.left)
        if self.prev_node:
            self.min_value = min(self.min_value, abs(self.prev_node.val - root.val))
        self.prev_node = root
        self.visitRoot(root.right)


node1 = TreeNode(1)
node5 = TreeNode(5)
node4 = TreeNode(4)
node9 = TreeNode(9)
node8 = TreeNode(9, left=node9)
node7 = TreeNode(7, right=node8)
node3 = TreeNode(3, left=node4, right=node5)
node2 = TreeNode(2, left=node1, right=node3)
node6 = TreeNode(6, left=node2, right=node7)
solution = Solution()
print(solution.minDiffInBST(node6))
