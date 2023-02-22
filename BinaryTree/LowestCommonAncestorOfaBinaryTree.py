class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.ancestor = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.find_ancestor(root, p, q)
        return self.ancestor

    def find_ancestor(self, node: TreeNode, p: 'TreeNode', q: 'TreeNode') -> bool:
        if node is None or self.ancestor:
            return False

        is_left_descendant = self.find_ancestor(node.left, p, q)
        is_right_descendant = self.find_ancestor(node.right, p, q)
        am_i_descendant = node.val == p.val or node.val == q.val

        if sum([is_left_descendant, is_right_descendant, am_i_descendant]) >= 2:
            if not self.ancestor:
                self.ancestor = node

        return is_left_descendant or is_right_descendant or am_i_descendant

