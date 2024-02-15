# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head) -> int:
        slow, fast = head, head
        while (fast):  # get slow to point on middle node
            slow = slow.next
            fast = fast.next.next
        midNode = self.reverse(slow)
        curNode = head
        maxSum = 0
        while(midNode):
            maxSum = max(maxSum, midNode.val + curNode.val)
            midNode = midNode.next
            curNode = curNode.next
        return maxSum

    def reverse(self,head):
        prev, cur = head, head.next
        prev.next = None
        while(cur):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

if __name__ == '__main__':
    sol = Solution()
    # head = ListNode(5,ListNode(4,ListNode(2,ListNode(1))))
    # head = ListNode(4,ListNode(2,ListNode(2,ListNode(3))))
    head = ListNode(1,ListNode(10000))
    maxSum = sol.pairSum(head)
    print(maxSum)