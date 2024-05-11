class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smaller = ListNode()
        greater = ListNode()
        sHead, gHead = smaller, greater
        if not head or not head.next:
            return head
        node = head
        while node:
            if node.val < x:
                temp = node.next
                smaller.next = node
                smaller = smaller.next
                smaller.next = None
                node = temp
            else:  # greater
                temp = node.next
                greater.next = node
                greater = greater.next
                greater.next = None
                node = temp
        temp = gHead.next
        gHead.next = None
        gHead = temp
        smaller.next = gHead
        temp = sHead.next
        sHead.next = None
        return temp


if __name__ == '__main__':
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    sol = Solution()
    h = sol.partition(head, 3)
    a = 5
