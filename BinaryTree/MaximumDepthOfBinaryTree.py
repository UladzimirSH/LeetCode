from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_node_depth = self.maxDepth(root.left)
        right_node_depth = self.maxDepth(root.right)
        return max(left_node_depth, right_node_depth) + 1


node1 = TreeNode(1)
node5 = TreeNode(5)
node4 = TreeNode(4)
node9 = TreeNode(9)
node8 = TreeNode(8, left=node9)
node7 = TreeNode(7, right=node8)
node3 = TreeNode(3, left=node4, right=node5)
node2 = TreeNode(2, left=node1, right=node3)
node6 = TreeNode(6, left=node2, right=node7)
solution = Solution()
print(solution.maxDepth(node6))