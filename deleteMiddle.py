# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        mid, fast = head, head
        while (fast and fast.next):
            mid = mid.next
            fast = fast.next.next
        prev = head
        while prev.next != mid:
            prev = prev.next
        prev.next = mid.next
        mid.next = None
        return head
