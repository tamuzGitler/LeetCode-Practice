# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, cur = head, head.next
        prev.next = None
        while (prev != None):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
