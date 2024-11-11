# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        mid, fast = head, head
        prev = None
        while fast and fast.next:
            prev = mid
            mid = mid.next
            fast = fast.next.next
        mid = self.reverseList(mid)
        node = head
        maxPair = 0
        while mid != None:
            maxPair = max(maxPair, mid.val + node.val)
            mid = mid.next
            node = node.next
        return maxPair

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        node = head
        while node:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
        return prev
