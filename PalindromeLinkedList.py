# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:

        length = 0
        curNode = head
        while(curNode):
            curNode = curNode.next
            length += 1
        if length == 1:
            return True
        if length == 2:
            return head.val == head.next.val
        midLength = length // 2 if length %2 == 0 else length//2 +1
        curNode = head
        for i in range(midLength):
            curNode = curNode.next
        curNode = self.reverse(curNode)
        for i in range(length // 2):
            if curNode.val != head.val:
                return False
            curNode = curNode.next
            head = head.next
        return True
    def reverse(self,head):
         nextNode = head.next
         prevNode = head
         prevNode.next = None
         while(nextNode):
             temp = nextNode.next
             nextNode.next = prevNode
             prevNode = nextNode
             nextNode = temp
         return prevNode

if __name__ == '__main__':
    head = ListNode(1,ListNode(1,ListNode(2,ListNode(1))))
    sol = Solution()
    # t = sol.reverse(head)
    print(sol.isPalindrome(head))
    a =5