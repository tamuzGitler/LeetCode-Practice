# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        if not head or not head.next:
            return None
        slow, fast = head, head
        shift = 0
        while( shift < n):
            fast = fast.next
            shift += 1
            if not fast:
                return head.next

        while(fast.next):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    # head = ListNode(4,ListNode(2,ListNode(2,ListNode(3))))
    # head = ListNode(1)
    head = sol.removeNthFromEnd(head,3)
    print(head)
