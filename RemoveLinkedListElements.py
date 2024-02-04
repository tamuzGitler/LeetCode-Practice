# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
   
        cur = head
        while (cur and cur.val == val):
            cur = cur.next
        retHead = cur

        while (cur and cur.next):
            temp = cur.next
            while (temp and temp.val == val):
                temp = temp.next
            cur.next = temp
            cur = cur.next
        return retHead
if __name__ == '__main__':
    head = ListNode(1, ListNode(2,ListNode(2,ListNode(1))))
    sol  = Solution()
    removedValList = sol.removeElements(head,2)
    a = 5

