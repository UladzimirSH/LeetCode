import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     prev_val = -math.inf
    #     if root.left and not self.isValidBST(root.left):
    #         return False
    #     if prev_val >= root.val:
    #         return False
    #     prev_val = root.val
    #     if root.right and not self.isValidBST(root.right):
    #         return False
    #     return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        prev_value = -math.inf
        stack = []
        head = root
        while stack or head:
            while head:
                stack.append(head)
                head = head.left

            # visit node
            head = stack.pop()
            if prev_value >= head.val:
                return False
            prev_value = head.val
            head = head.right
        return True


node1 = TreeNode(1)
node3 = TreeNode(3)
node2 = TreeNode(2, left=node1, right=node3)
solution = Solution()
solution.isValidBST(node2)