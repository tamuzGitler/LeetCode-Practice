# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        prev = ListNode(0, head)
        flag = True
        retHead = head
        while node and node.next:
            # x -> y -> z into y -> x -> z
            x = node
            y = node.next
            z = node.next.next
            y.next = x
            x.next = z
            prev.next = y
            if flag:
                retHead = y
                flag = False
            prev = x
            node = z
        return retHead
