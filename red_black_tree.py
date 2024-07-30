class Node:
    def __init__(self, key, color='red', left=None, right=None, parent=None):
        # Initialize a new node with the given key, color, left child, right child, and parent
        self.key = key  # The key or value stored in the node
        self.color = color  # The color of the node, either 'red' or 'black'
        self.left = left  # Reference to the left child node
        self.right = right  # Reference to the right child node
        self.parent = parent  # Reference to the parent node

class RedBlackTree:
    def __init__(self):
        # Initialize the Red-Black Tree with a NIL node and root
        self.NIL = Node(key=None, color='black')  # Create a sentinel NIL node which is always black
        self.root = self.NIL  # Initially, the tree is empty, so the root is the NIL node

    def insert(self, key):
        # Insert a new node with the given key into the Red-Black Tree
        new_node = Node(key)  # Create a new node with the given key, default color is red
        new_node.left = self.NIL  # The new node's left child is the NIL node
        new_node.right = self.NIL  # The new node's right child is the NIL node
        new_node.color = 'red'  # New nodes are initially red

        parent = None  # Parent of the new node, initially None
        current = self.root  # Start from the root

        # Traverse the tree to find the correct position for the new node
        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        # Set the parent of the new node
        new_node.parent = parent

        # If the tree is empty, set the new node as the root
        if parent is None:
            self.root = new_node
        # Otherwise, set the new node as the left or right child of the parent
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # If the new node is the root, set its color to black and return
        if new_node.parent is None:
            new_node.color = 'black'
            return

        # If the new node has no grandparent, return
        if new_node.parent.parent is None:
            return

        # Fix any violations of the Red-Black Tree properties
        self.fix_insert(new_node)

    def left_rotate(self, node):
        # Perform a left rotation on the given node
        y = node.right  # Set y to the right child of node
        node.right = y.left  # Turn y's left subtree into node's right subtree
        if y.left != self.NIL:
            y.left.parent = node  # Update parent of y's left subtree
        y.parent = node.parent  # Link y's parent to node's parent
        if node.parent is None:
            self.root = y  # If node is root, set y as the new root
        elif node == node.parent.left:
            node.parent.left = y  # If node is a left child, set y as the left child of node's parent
        else:
            node.parent.right = y  # If node is a right child, set y as the right child of node's parent
        y.left = node  # Put node on y's left
        node.parent = y  # Update node's parent

    def right_rotate(self, node):
        # Perform a right rotation on the given node
        y = node.left  # Set y to the left child of node
        node.left = y.right  # Turn y's right subtree into node's left subtree
        if y.right != self.NIL:
            y.right.parent = node  # Update parent of y's right subtree
        y.parent = node.parent  # Link y's parent to node's parent
        if node.parent is None:
            self.root = y  # If node is root, set y as the new root
        elif node == node.parent.right:
            node.parent.right = y  # If node is a right child, set y as the right child of node's parent
        else:
            node.parent.left = y  # If node is a left child, set y as the left child of node's parent
        y.right = node  # Put node on y's right
        node.parent = y  # Update node's parent

    def fix_insert(self, node):
        # Fix the Red-Black Tree properties after inserting a new node
        while node.parent.color == 'red':
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left  # Get the uncle node
                if uncle.color == 'red':
                    # Case 1: Uncle is red
                    uncle.color = 'black'  # Recolor uncle to black
                    node.parent.color = 'black'  # Recolor parent to black
                    node.parent.parent.color = 'red'  # Recolor grandparent to red
                    node = node.parent.parent  # Move node to grandparent
                else:
                    if node == node.parent.left:
                        # Case 2: Node is left child
                        node = node.parent
                        self.right_rotate(node)  # Perform right rotation
                    # Case 3: Node is right child
                    node.parent.color = 'black'  # Recolor parent to black
                    node.parent.parent.color = 'red'  # Recolor grandparent to red
                    self.left_rotate(node.parent.parent)  # Perform left rotation
            else:
                uncle = node.parent.parent.right  # Get the uncle node
                if uncle.color == 'red':
                    # Case 1: Uncle is red
                    uncle.color = 'black'  # Recolor uncle to black
                    node.parent.color = 'black'  # Recolor parent to black
                    node.parent.parent.color = 'red'  # Recolor grandparent to red
                    node = node.parent.parent  # Move node to grandparent
                else:
                    if node == node.parent.right:
                        # Case 2: Node is right child
                        node = node.parent
                        self.left_rotate(node)  # Perform left rotation
                    # Case 3: Node is left child
                    node.parent.color = 'black'  # Recolor parent to black
                    node.parent.parent.color = 'red'  # Recolor grandparent to red
                    self.right_rotate(node.parent.parent)  # Perform right rotation
            if node == self.root:
                break  # If node is root, break the loop
        self.root.color = 'black'  # Ensure the root is black

    def search(self, key):
        # Search for a node with the given key in the Red-Black Tree
        current = self.root  # Start from the root
        while current != self.NIL:
            if current.key == key:
                return current  # Return the node if found
            elif key < current.key:
                current = current.left  # Move to the left child
            else:
                current = current.right  # Move to the right child
        return None  # Return None if the key is not found

    def in_order_traversal(self, node, result=None):
        # Perform an in-order traversal of the tree
        if result is None:
            result = []  # Initialize the result list if not provided
        if node != self.NIL:
            self.in_order_traversal(node.left, result)  # Traverse the left subtree
            result.append(node.key)  # Visit the current node
            self.in_order_traversal(node.right, result)  # Traverse the right subtree
        return result  # Return the result list
