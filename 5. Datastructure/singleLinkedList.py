class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
    def prepend(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        temp = self.head
        self.head = newNode
        self.head.next = temp
    def delete(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if current.next:
            temp = current.next
            current.next = current.next.next
            del temp
    def print(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")
            