# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        decimal = 0
        node = head

        while node:
            decimal = decimal << 1  # shift - power by 2
            decimal += node.val
            node = node.next
        return decimal


if __name__ == '__main__':
    head = ListNode(1, ListNode(1, ListNode(1)))
    sol = Solution()
    print(sol.getDecimalValue(head))
    print(2 << 1)
