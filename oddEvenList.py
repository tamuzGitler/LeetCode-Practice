# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        retHead = head
        even = ListNode()
        demi = even
        node = head
        while (node and node.next):
            evenNode = node.next

            node.next = node.next.next
            demi.next = evenNode
            evenNode.next = None
            demi = demi.next
            if node.next:
                node = node.next
        node.next = even.next
        return retHead


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    sol = Solution()
    sol.oddEvenList(head)
    a = 5
