class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None
    
    def insert(self, item):
        node = Node(item)
        if self.head == None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def remove(self, item):
        if self.head.item == item:
            if self.head.next == None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return
        
        prev = None
        current = self.head
        while current.item != item:
            prev = current
            current = current.next
        if current == self.tail:
            prev.next = None
            self.tail = prev
        else:
            prev.next = current.next

    def __iter__(self):
        return LinkedListIterator(self.head)
    
class LinkedListIterator:
    def __init__(self, head):
        self.current = head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            value = self.current.item
            self.current = self.current.next
            return value
