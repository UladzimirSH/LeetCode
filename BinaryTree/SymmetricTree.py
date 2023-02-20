from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_queue = [root.left]
        right_queue = [root.right]

        while left_queue and right_queue:
            if left_queue and not right_queue:
                return False
            if right_queue and not left_queue:
                return False

            left_node = left_queue.pop(0)
            right_node = right_queue.pop(0)

            if not left_node and not right_node:
                continue

            if left_node and not right_node:
                return False
            if right_node and not left_node:
                return False

            if left_node.val != right_node.val:
                return False

            left_queue.append(left_node.left)
            right_queue.append(right_node.right)

            left_queue.append(left_node.right)
            right_queue.append(right_node.left)

        return True


# node3left = TreeNode(3)
# node4left = TreeNode(4)
# node3right = TreeNode(3)
# node4right = TreeNode(4)
# node2left = TreeNode(2, left=node3left, right=node4left)
# node2right = TreeNode(2, left=node4right, right=node3right)
# node1 = TreeNode(1, left=node2left, right=node2right)
node0 = TreeNode(0)
node1 = TreeNode(1, left=node0)
solution = Solution()
print(solution.isSymmetric(node1))