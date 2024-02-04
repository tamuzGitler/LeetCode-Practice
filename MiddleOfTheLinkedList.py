# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow, fast = head, head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    sol = Solution()
    # print(sol.middleNode(head1).val)
    print(sol.middleNode(head2).val)