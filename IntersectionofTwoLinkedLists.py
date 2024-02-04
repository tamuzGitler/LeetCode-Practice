# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # l1,l2 = headA, headB
        # while l1 != l2:
        #     l1 = l1.next if l1 else headB
        #     l2 = l2.next if l2 else headA
        # return l1
        lenA,lenB = 0,0
        l1,l2 = headA,headB
        while (l1):
            lenA += 1
            l1 = l1.next
        while (l2):
            lenB += 1
            l2 = l2.next
        dif = abs(lenA - lenB)
        l1, l2 = headA, headB
        if lenA > lenB:
            while(dif>0):
                l1 = l1.next
                dif-=1
        else:
            while (dif > 0):
                l2 = l2.next
                dif -= 1
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next
        return l1



if __name__ == '__main__':
    headA = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
    headB = ListNode(5,ListNode(6,ListNode(1,headA.next.next)))
    sol = Solution()
    print(sol.getIntersectionNode(headA,headB).val)
