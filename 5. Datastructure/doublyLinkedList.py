class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    def delete(self, key):
        current = self.head
        while current:
            if current.value == key:
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current.next is None:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
            current = current.next

    def display_forward(self):
        if not self.head:
            return
        current = self.head
        while current:
            print(current.value, end = " -> ")
            current = current.next
        print("None")
    def display_backward(self):
        if not self.head:
            return
        current = self.tail
        while current:
            print(current.value, end=" -> ")
            current = current.prev
        print("None")
