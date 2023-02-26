from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.root = root

    def next(self) -> int:
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        self.root = self.stack.pop()
        next_value = self.root.val
        self.root = self.root.right
        return next_value

    def hasNext(self) -> bool:
        return self.stack or self.root


# Your BSTIterator object will be instantiated and called as such:
root = TreeNode(1)
obj = BSTIterator(root)
param_1 = obj.hasNext()
param_2 = obj.hasNext()
