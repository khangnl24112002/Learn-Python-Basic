from singleLinkedList import LinkedList
from doublyLinkedList import DoublyLinkedList
from bst import BST

ll = LinkedList()

ll.append(1)
ll.append(4)
ll.append(7)
ll.prepend(0)
ll.delete(7)

ll.print()

bst = BST()
nums = [0, 4, 2, 9, 5, 6, 8, 1, 7, 3]
for num in nums:
    bst.insert(num)
    
bst.delete(5)
print(bst.inorder())

dll = DoublyLinkedList()
for num in nums:
    dll.append(num)
dll.delete(4)
dll.delete(3)
# dll.display_forward()