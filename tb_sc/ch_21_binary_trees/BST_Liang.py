# Original BST from Liangs ch 19
# There are comments in the code that point out where the original code 
# had issues and how it was refactored to be more Pythonic.

class BST:
    def __init__(self):
        # Java-like public fields; refactor uses internal names (_root, _size).
        self.root = None
        self.size = 0

    # Return True if the element is in the tree 
    def search(self, e):
        current = self.root # Start from the root

        # Java-like None check (!= None); Pythonic form is: is not None
        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True # Element is found

        return False
    
    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully 
    def insert(self, e):
        # Java-like None check (== None); Pythonic form is: is None
        if self.root == None:
            # Java-like camelCase helper name; refactor uses _new_node(...)
            self.root = self.createNewNode(e) # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            # Java-like None check (!= None); Pythonic form is: is not None
            while current != None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                # Java-style helper naming kept here for textbook parity.
                parent.left = self.createNewNode(e)
            else:
                parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    # Java-like method naming; Pythonic style is snake_case (_new_node).
    def createNewNode(self, e):
        return TreeNode(e)

    # Return the size of the tree
    # Java-like getter (getSize); Pythonic style is len(tree) via __len__.
    def getSize(self):
        return self.size
    
    # Inorder traversal from the root
    def inorder(self):
        # Java-like public helper call; refactor uses private helper _inorder.
        self.inorderHelper(self.root)

    # Inorder traversal from a subtree 
    def inorderHelper(self, r):
        # Java-like None check (!= None); Pythonic form is: is not None
        if r != None:
            self.inorderHelper(r.left)
            print(r.element, end = " ")
            self.inorderHelper(r.right)

    # Postorder traversal from the root 
    def postorder(self):
        # Java-like public helper call; refactor uses private helper _postorder.
        self.postorderHelper(self.root)

    # Postorder traversal from a subtree 
    def postorderHelper(self, root):
        # Java-like None check (!= None); Pythonic form is: is not None
        if root != None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end = " ")

    # Preorder traversal from the root 
    def preorder(self):
        # Java-like public helper call; refactor uses private helper _preorder.
        self.preorderHelper(self.root)

    # Preorder traversal from a subtree 
    def preorderHelper(self, root):
        # Java-like None check (!= None); Pythonic form is: is not None
        if root != None:
            print(root.element, end = " ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

    # Returns a path from the root leading to the specified element 
    def path(self, e):
        # Shadows built-in list; refactor renames this variable to nodes.
        list = []
        current = self.root # Start from the root

        # Java-like None check (!= None); Pythonic form is: is not None
        while current != None:
            list.append(current) # Add the node to the list
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break

        return list # Return an array of nodes

    # Delete an element from the binary search tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree 
    def delete(self, e):
        # Locate the node to be deleted and its parent node
        parent = None
        current = self.root
        # Java-like None check (!= None); Pythonic form is: is not None
        while current != None:
            if e < current.element:
                parent = current
                current = current.left
            elif e > current.element: 
                parent = current
                current = current.right
            else:
                break # Element is in the tree pointed by current

        # Java-like None check (== None); Pythonic form is: is None
        if current == None:
            return False # Element is not in the tree

        # Case 1: current has no left children
        # Java-like None check (== None); Pythonic form is: is None
        if current.left == None:
            # Connect the parent with the right child of the current node
            # Java-like None check (== None); Pythonic form is: is None
            if parent == None:
                self.root = current.right
            else:
                if e < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right
        else:
            # Case 2: The current node has a left child
            # Locate the rightmost node in the left subtree of
            # the current node and also its parent
            # Java-like camelCase variable; refactor uses parent_of_rightmost.
            parentOfRightMost = current
            # Java-like camelCase variable; refactor uses rightmost.
            rightMost = current.left

            # Java-like None check (!= None); Pythonic form is: is not None
            while rightMost.right != None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right # Keep going to the right

            # Replace the element in current by the element in rightMost
            current.element = rightMost.element

            # Eliminate rightmost node
            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
                # Special case: parentOfRightMost == current
                parentOfRightMost.left = rightMost.left     

        self.size -= 1
        return True # Element deleted

    # Return true if the tree is empty
    # Java-like method name; Pythonic style is is_empty().
    def isEmpty(self):
        return self.size == 0
        
    # Remove all elements from the tree
    def clear(self):
        # Bug: these lines compare instead of assign.
        # Refactor uses: self._root = None and self._size = 0
        self.root = None
        self.size = 0

    # Return the root of the tree
    # Java-like getter (getRoot); Pythonic style is direct attribute/property access.
    def getRoot(self):
        return self.root

class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None
