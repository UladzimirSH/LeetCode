from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # def __init__(self):
    #     self.reversed_node = None
    #
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None
    #     if not head.next:
    #         return head
    #
    #     def reverse_internal(head: Optional[ListNode], next: Optional[ListNode]):
    #         if not next:
    #             head.next = None
    #             self.reversed_node = head
    #             return
    #         reverse_internal(next, next.next)
    #         next.next = head
    #
    #     reverse_internal(head, head.next)
    #     head.next = None
    #     return self.reversed_node

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        prev = head
        next = head.next

        head.next = None

        while prev and next:
            after_next = next.next
            next.next = prev

            prev = next
            next = after_next

        return prev


solution = Solution()
t = solution.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
print(t)
