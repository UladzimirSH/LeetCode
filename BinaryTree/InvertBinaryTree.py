from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.visit_tree(root)
        return root

    def visit_tree(self, root: Optional[TreeNode]):
        if root is None:
            return

        temp = root.left
        root.left = root.right
        root.right = temp
        self.visit_tree(root.left)
        self.visit_tree(root.right)


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
print(solution.invertTree(node6))