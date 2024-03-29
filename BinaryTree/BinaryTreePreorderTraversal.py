from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.values = []
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if root is None:
    #         return []
    #
    #     stack = []
    #     values = []
    #     stack.append(root)
    #
    #     while stack:
    #         node = stack.pop()
    #         values.append(node.val)
    #         if node.right:
    #             stack.append(node.right)
    #
    #         if node.left:
    #             stack.append(node.left)
    #
    #     return values

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        self.visitNode(root)
        return self.values

    def visitNode(self, node: TreeNode):
        self.values.append(node.val)
        if node.left:
            self.visitNode(node.left)
        if node.right:
            self.visitNode(node.right)


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
print(solution.preorderTraversal(node6))  # [1, 4, 5, 3, 2, 9, 8, 7, 6]
