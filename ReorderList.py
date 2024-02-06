# Definition for singly-linked list.
import math


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        length = 0
        cur = head
        while(cur):
            length += 1
            cur = cur.next
        p2 = head
        prev  = None

        for i in range(math.ceil(length / 2)):
            prev = p2
            p2 = p2.next
        p2 = self.reverseList(p2)
        prev.next =None
        p1 = head # p2 is ready
        while(p2):
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2

        return head

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        prev, cur = head, head.next
        prev.next = None
        while (cur != None):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


if __name__ == '__main__':
    sol = Solution()
    l = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    l =sol.reorderList(l)
    a = 4
