# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        curNode = head
        node1 = l1
        node2 = l2
        rest = 0
        while (node1 or node2 or rest):
            curNode.next = ListNode()
            curNode = curNode.next
            curVal = rest
            curVal += node1.val if node1 else 0
            curVal += node2.val if node2 else 0
            rest = curVal // 10
            curVal = curVal % 10
            curNode.val = curVal
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
        return head.next


if __name__ == '__main__':
    l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
    # l1 = ListNode(2,ListNode(4,ListNode(3)))
    l2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9))))
    # l2 = ListNode(5,ListNode(6,ListNode(4)))
    sol = Solution()
    head = sol.addTwoNumbers(l1, l2)
    a = 5
