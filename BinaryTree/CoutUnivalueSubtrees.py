from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.counter = 0

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.visit_and_count(root)
        return self.counter

    def visit_and_count(self, node: Optional[TreeNode]) -> bool:
        if not node.left and not node.right:
            self.counter += 1
            return True

        is_uni = True
        if node.left:
            is_uni = self.visit_and_count(node.left) and is_uni and node.left.val == node.val
        if node.right:
            is_uni = self.visit_and_count(node.right) and is_uni and node.right.val == node.val

        if is_uni:
            self.counter += 1
            return True

        return False

print(1//2)

node1 = TreeNode(5, left=TreeNode(5), right=TreeNode(5))
node5 = TreeNode(5, right=TreeNode(5))
node55 = TreeNode(5, left=node1, right=node5)
# node55 = TreeNode(5, left=TreeNode(5), right=TreeNode(1))
solution = Solution()
print(solution.countUnivalSubtrees(node55))
