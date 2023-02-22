from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        leftmost = root
        while leftmost:
            head = leftmost
            prev = None
            leftmost = None
            while head:
                if head.left:
                    if not leftmost:
                        leftmost = head.left
                    if prev:
                        prev.next = head.left
                    prev = head.left
                if head.right:
                    if not leftmost:
                        leftmost = head.right
                    if prev:
                        prev.next = head.right
                    prev = head.right
                head = head.next
        return root


node5 = Node(5)
node7 = Node(7)
node8 = Node(8)
node6 = Node(6, left=node7)
node4 = Node(4, left=node8)
node2 = Node(2, right=node6)
node3 = Node(3, left=node4, right=node5)
node1 = Node(1, left=node2, right=node3)
solution = Solution()
print(solution.connect(node1))


