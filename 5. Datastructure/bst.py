class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)
    def search(self, value):
        return self._search(self.root, value)
    def _search(self, current, value):
        if current is None:
            return False
        elif current.value == value:
            return True
        elif value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)
    def delete(self, value):
        self.root = self._delete(self.root, value)
    def _delete(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None: 
                return node.left
            else:
                min_larger_node = self._min_value_node(node.right)
                node.value = min_larger_node.value
                node.right = self._delete(node.right, min_larger_node.value)
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
        

        

