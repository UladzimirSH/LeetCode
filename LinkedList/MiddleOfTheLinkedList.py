from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        current_middle = head
        current_head = head
        while current_head and current_head.next:
            current_middle = current_middle.next
            current_head = current_head.next.next

        return current_middle
