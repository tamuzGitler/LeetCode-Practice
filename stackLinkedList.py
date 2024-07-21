class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class StackLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return (self.head == None) and (self.tail == None)

    def peek(self):
        try:
            val = self.head.val
        except:
            return None
        return val

    def pop(self):
        if not self.isEmpty():
            topVal = self.head.val
            nextNode = self.head.next
            self.head.next = None
            self.head = nextNode
            if self.head == None:
                self.tail = self.head
            return topVal

    def push(self, val):
        if (self.head == None) and (self.tail == None):
            self.head = ListNode(val)
            self.tail = self.head
        else:
            self.head = ListNode(val, self.head)


if __name__ == '__main__':
    stackLinkedList = StackLinkedList()
    print(stackLinkedList.isEmpty())
    print(stackLinkedList.peek())
    stackLinkedList.push(1)
    stackLinkedList.push(2)
    stackLinkedList.push(3)
    print(stackLinkedList.pop())
    print(stackLinkedList.pop())
    print(stackLinkedList.pop())

    stackLinkedList.push(3)
    a = 5
