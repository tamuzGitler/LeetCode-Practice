# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow, fast, endOfFirstList = head, head, head
        # find mid node
        while fast and fast.next:
            endOfFirstList = slow
            slow = slow.next
            fast = fast.next.next
        endOfFirstList.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)

    def merge(self, head1, head2):
        head = ListNode()
        h = head
        while head1 or head2:
            # if not head1
            # if not head2
            if not head2 or (head1 and head1.val < head2.val):
                temp = head1.next
                head.next = head1
                head1.next = None
                head1 = temp
            elif not head1 or (head2 and head1.val >= head2.val):
                temp = head2.next
                head.next = head2
                head2.next = None
                head2 = temp
            head = head.next
        return h.next


if __name__ == '__main__':
    head = ListNode(5, ListNode(4, ListNode(3, ListNode(2))))
    sol = Solution()
    head = sol.sortList(head)
    a = 5
