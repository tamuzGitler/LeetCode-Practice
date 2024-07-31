# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = head
        stack = []
        while (node):

            while stack and stack[-1].val < node.val:
                stack.pop()
            if stack:
                stack[-1].next = node
            stack.append(node)
            node = node.next

        return stack[0]
