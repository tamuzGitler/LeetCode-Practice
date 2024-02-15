# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        slow,fast = head, head

        for i in range(1,k):
            fast = fast.next
        left = fast

        while(fast.next):
            fast = fast.next
            slow = slow.next
        temp = left.val
        left.val = slow.val
        slow.val = temp
        return head

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    # head = ListNode(4,ListNode(2,ListNode(2,ListNode(3))))
    # head = ListNode(1)
    head = sol.swapNodes(head,2)
    print(head)


