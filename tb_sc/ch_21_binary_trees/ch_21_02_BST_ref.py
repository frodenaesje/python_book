# file: ch_21_02_BST_ref.py
"""This code is refactored from a textbook which had
a "Java" type implementation of a binary search tree (BST).
The code below is more Pythonic and
includes type annotations for better readability and error checking.
The core functionality of the binary search tree (BST) remains intact,
but the code is structured in a way that is more idiomatic to Python.
Type annotations are used to clarify the expected types of variables
and function parameters, which can help with debugging
and understanding the code.
The code can serve as a starting point for several exercises related to binary search trees, such as
- implementing additional methods"""

# Any reads as: "can be any type".
from typing import Any

class BST:
    def __init__(self) -> None:
        # TreeNode | None reads as: "either a TreeNode or None".
        self._root: TreeNode | None = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    # Any reads as: "can be any type"
    def __contains__(self, value: Any) -> bool:
        return self.search(value)

    def is_empty(self) -> bool:
        return self._size == 0

    def search(self, value: Any) -> bool:
        current = self._root
        while current is not None:
            if value < current.element:
                current = current.left
            elif value > current.element:
                current = current.right
            else:
                return True
        return False

    def insert(self, value: Any) -> bool:
        if self._root is None:
            self._root = self._new_node(value)
            self._size += 1
            return True

        parent: TreeNode | None = None
        current = self._root
        while current is not None:
            parent = current
            if value < current.element:
                current = current.left
            elif value > current.element:
                current = current.right
            else:
                return False

        if parent is None:
            return False

        if value < parent.element:
            parent.left = self._new_node(value)
        else:
            parent.right = self._new_node(value)

        self._size += 1
        return True

    def _new_node(self, value: Any) -> "TreeNode":
        return TreeNode(value)

    def inorder(self) -> None:
        self._inorder(self._root)

    def _inorder(self, node: "TreeNode | None") -> None:
        if node is not None:
            self._inorder(node.left)
            print(node.element, end=" ")
            self._inorder(node.right)

    def preorder(self) -> None:
        self._preorder(self._root)

    def _preorder(self, node: "TreeNode | None") -> None:
        if node is not None:
            print(node.element, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self) -> None:
        self._postorder(self._root)

    def _postorder(self, node: "TreeNode | None") -> None:
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.element, end=" ")

    # list["TreeNode"] reads as: "a list of TreeNode objects".
    def path(self, value: Any) -> list["TreeNode"]:
        nodes: list[TreeNode] = []
        current = self._root

        while current is not None:
            nodes.append(current)
            if value < current.element:
                current = current.left
            elif value > current.element:
                current = current.right
            else:
                break

        return nodes

    def delete(self, value: Any) -> bool:
        parent: TreeNode | None = None
        current = self._root

        while current is not None:
            if value < current.element:
                parent = current
                current = current.left
            elif value > current.element:
                parent = current
                current = current.right
            else:
                break

        if current is None:
            return False

        if current.left is None:
            if parent is None:
                self._root = current.right
            elif value < parent.element:
                parent.left = current.right
            else:
                parent.right = current.right
        else:
            parent_of_rightmost = current
            rightmost = current.left

            while rightmost.right is not None:
                parent_of_rightmost = rightmost
                rightmost = rightmost.right

            current.element = rightmost.element

            if parent_of_rightmost.right == rightmost:
                parent_of_rightmost.right = rightmost.left
            else:
                parent_of_rightmost.left = rightmost.left

        self._size -= 1
        return True

    def clear(self) -> None:
        self._root = None
        self._size = 0

class TreeNode:
    def __init__(self, element: Any) -> None:
        self.element = element
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


if __name__ == "__main__":
    bst = BST()

    print("Insert values:")
    for value in [60, 55, 100, 45, 57, 67, 107, 59, 101]:
        print(f"insert({value}) -> {bst.insert(value)}")

    print("\nSize:", len(bst))
    print("Search 67:", bst.search(67))
    print("Search 99:", bst.search(99))

    print("\nInorder traversal:", end=" ")
    bst.inorder()
    print()

    print("Preorder traversal:", end=" ")
    bst.preorder()
    print()

    print("Postorder traversal:", end=" ")
    bst.postorder()
    print()

    print("\nDelete 55:", bst.delete(55))
    print("Delete 99:", bst.delete(99))
    print("Size after delete:", len(bst))

    print("\nInorder after delete:", end=" ")
    bst.inorder()
    print()
