# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow, fast = head, head
        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next
            if slow == fast:
                while fast != head:
                    head = head.next
                    fast = fast.next
                return head
        return None


if __name__ == '__main__':
    node = ListNode(1)
    node2 = ListNode(2)
    node.next = node2
    node2.next = node
    sol = Solution()
    print(sol.detectCycle(node).val)
