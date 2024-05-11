class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if (head.next == None and n == 1):
            return None
        slow = head
        fast = head
        i = 0
        while (i < n):
            fast = fast.next
            i += 1
        if not fast: return head.next

        while (fast.next):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    l = ListNode(1, ListNode(2))
    sol = Solution()
    a = sol.removeNthFromEnd(l, 2)
    b = 5
