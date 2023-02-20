from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.has_target_sum = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        self.find_target_sum(root, targetSum)

        return self.has_target_sum

    def find_target_sum(self, node: TreeNode, current_sum: int):
        if node is None:
            return

        if self.has_target_sum:
            return

        current_sum -= node.val
        # if we reach leaf and get the target sum
        if current_sum == 0 and not node.left and not node.right:
            self.has_target_sum = True
            return

        self.find_target_sum(node.left, current_sum)
        self.find_target_sum(node.right, current_sum)