class TreeNode:
    def __init__(self, key):
        self.key = key  # Initialize the key value of the node
        self.left = None  # Initialize the left child pointer to None
        self.right = None  # Initialize the right child pointer to None

    def __str__(self):
        return str(self.key)  # Convert the key to a string for printing


class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize the root of the binary search tree to None

    def insert(self, key):
        self.root = self._insert(self.root, key)  # Insert a key into the binary search tree

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)  # If the current node is None, create a new node with the key
        if key < node.key:
            node.left = self._insert(node.left, key)  # Recursively insert into the left subtree
        elif key > node.key:
            node.right = self._insert(node.right, key)  # Recursively insert into the right subtree
        return node

    def search(self, key):
        return self._search(self.root, key)  # Search for a key in the binary search tree

    def _search(self, node, key):
        if node is None or node.key == key:
            return node  # Return the node if found or None if not found
        if key < node.key:
            return self._search(node.left, key)  # Recursively search the left subtree
        return self._search(node.right, key)  # Recursively search the right subtree

    def delete(self, key):
        self.root = self._delete(self.root, key)  # Delete a key from the binary search tree

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)  # Recursively delete from the left subtree
        elif key > node.key:
            node.right = self._delete(node.right, key)  # Recursively delete from the right subtree
        else:
            if node.left is None:
                return node.right  # Replace the node with its right child
            elif node.right is None:
                return node.left  # Replace the node with its left child
            node.key = self._min_value(node.right)  # Replace the node with the minimum value from the right subtree
            node.right = self._delete(node.right, node.key)  # Delete the minimum value from the right subtree
        return node

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key  # Find the minimum value in the subtree rooted at the given node

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)  # Perform an inorder traversal of the binary search tree
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)  # Recursively traverse the left subtree
            result.append(node.key)  # Append the current node's key to the result list
            self._inorder_traversal(node.right, result)  # Recursively traverse the right subtree


bst = BinarySearchTree()  # Create an instance of BinarySearchTree
nodes = [50, 30, 20, 40, 70, 60, 80]  # Nodes to insert into the binary search tree

for node in nodes:
    bst.insert(node)  # Insert each node into the binary search tree
print("Inorder traversal:", bst.inorder_traversal())  # Print the inorder traversal of the binary search tree
print("Search for 40:", bst.search(40))  # Search for a key in the binary search tree
bst.delete(40)  # Delete a key from the binary search tree
print("Inorder traversal after deleting 40:", bst.inorder_traversal())  # Print the inorder traversal after deletion
