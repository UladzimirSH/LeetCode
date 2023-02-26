from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        p_was_found = False
        stack = []
        head = root
        while stack or head:
            while head:
                stack.append(head)
                head = head.left

            head = stack.pop()
            if p_was_found:
                return head
            if head.val == p.val:
                p_was_found = True

            head = head.right

        return None