from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        head = None
        if list1 and not list2:
            head = ListNode(list1.val)
            list1 = list1.next
        elif list2 and not list1:
            head = ListNode(list2.val)
            list2 = list2.next
        elif list1.val < list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next

        head.next = self.mergeTwoLists(list1, list2)
        return head


solution = Solution()
solution.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))))




