# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        retHead = head
        cur = head.next
        prev = head
        seeingValues = set()
        seeingValues.add(prev.val)
        while(cur):
            if cur.val in seeingValues:
                temp = cur.next
                prev.next = temp
                cur.next = None
                cur = temp
            else:
                seeingValues.add(cur.val)
                prev = cur
                cur = cur.next
        return retHead

if __name__ == '__main__':
    head = ListNode(1,ListNode(1,ListNode(2)))
    head2 = ListNode(1,ListNode(1,ListNode(2,ListNode(3,ListNode(3)))))
    sol = Solution()
    withoutDuplicate = sol.deleteDuplicates(head2)
    a=4


