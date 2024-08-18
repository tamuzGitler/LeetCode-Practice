# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        parts = []
        node = head
        n = 0
        while (node):
            n += 1
            node = node.next
        node = head
        partLen = n // k
        extras = n % k
        curPart = head
        curLen = 1

        for i in range(n):
            if curLen == (partLen + (1 if extras > 0 else 0)):
                parts.append(curPart)
                temp = node.next
                node.next = None
                node = temp
                extras -= 1
                curLen = 1
                curPart = node
            elif node:
                node = node.next
                curLen += 1

        return parts if (len(parts) == k) else parts + ([None] * (k - len(parts)))


def create_linked_list(head_values):
    dummy = ListNode()  # Dummy node to simplify insertion
    current = dummy

    for val in head_values:
        current.next = ListNode(val)
        current = current.next

    return dummy.next  # Head of the actual linked list


if __name__ == '__main__':
    head_values = [1, 2, 3]
    linked_list_head = create_linked_list(head_values)
    sol = Solution()
    print(len(sol.splitListToParts(linked_list_head, 5)))
    a = 5
