class Node:
    def __init__(self,key=-1):
        self.key = key
        self.next = None

class MyHashSet(object):

    def __init__(self):
        self.table = [Node() for i in range(1000)]
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        i = key % 1000
        if self.table[i].key == -1:
            self.table[i].key = key
        else:
            node = self.table[i]
            while(node.next):
                if node.key == key:
                    return
                node = node.next

            node.next = Node(key=key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        i = key % 1000
        node = self.table[i]

        while(node and node.next):
            node = node.next

        if node.next == key:
            node.next = None


    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        i = key % 1000
        node = self.table[i]
        while (node.next and node.key != key):
            node = node.next

        return node.key == key



if __name__ == '__main__':

# Your MyHashSet object will be instantiated and called as such:
    obj = MyHashSet()
    print(obj.add(1))
    print(obj.add(2))
    print(obj.remove(2))
    print(obj.contains(1))

