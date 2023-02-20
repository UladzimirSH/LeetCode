from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.values = []

    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if root is None:
    #         return []
    #
    #     stack = []
    #     values = []
    #     visited = {}
    #     stack.append(root)
    #
    #     while stack:
    #         node = stack.pop()
    #         visited[node] = 1
    #         if node.left and node.left not in visited:
    #             stack.append(node)
    #             stack.append(node.left)
    #             continue
    #         if node.right and node.right not in visited:
    #             stack.append(node)
    #             stack.append(node.right)
    #             continue
    #
    #         values.append(node.val)
    #     return values

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        self.visitNode(root)
        return self.values

    def visitNode(self, node: TreeNode):
        if node.left:
            self.visitNode(node.left)
        if node.right:
            self.visitNode(node.right)
        self.values.append(node.val)


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
print(solution.postorderTraversal(node6)) # [1, 4, 5, 3, 2, 9, 8, 7, 6]
