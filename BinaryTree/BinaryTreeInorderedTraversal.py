from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.values = []

    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []
    #
    #     stack = []
    #     values = []
    #     current = root
    #     while current or stack:
    #         while current:
    #             stack.append(current)
    #             current = current.left
    #         current = stack.pop()
    #         values.append(current.val)
    #         current = current.right
    #     return values

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        self.visitNode(root)
        return self.values

    def visitNode(self, node: TreeNode):
        if node.left:
            self.visitNode(node.left)
        self.values.append(node.val)
        if node.right:
            self.visitNode(node.right)




solution = Solution()
# node4 = TreeNode(4)
node3 = TreeNode(3)
node1 = TreeNode(1)
node10 = TreeNode(1)
node5 = TreeNode(5)
node7 = TreeNode(7)
node2 = TreeNode(2, left=node1, right=node3)
node4 = TreeNode(4, left=node2, right=node5)
print(solution.inorderTraversal(node1))
