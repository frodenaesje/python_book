# file: ch_21_01_binary_search_tree.py
# A classic implementation of a binary search tree (BST) in Python.
from collections import deque

class Node:
    def __init__(self, key: int):
        """Pseudocode:
        1. Set the left child to None.
        2. Set the right child to None.
        3. Store the node value.
        """
        self.left: "Node | None" = None
        self.right: "Node | None" = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        """Pseudocode:
        1. Start with an empty tree.
        2. The root is None.
        """
        self._root: "Node | None" = None
        self._size = 0

    def __len__(self) -> int:
        """Return number of nodes currently stored in the tree."""
        return self._size

    def is_empty(self) -> bool:
        """Pseudocode:
        1. Check whether the root is None.
        2. Return True if empty, otherwise False.
        """
        return self._root is None

    def _new_node(self, key: int) -> "Node":
        """Factory method so subclasses can override node type (e.g., AVL node)."""
        return Node(key)

    def insert(self, key: int) -> None:
        """Pseudocode:
        1. Create a new node with key.
        2. If the tree is empty, set it as root.
        3. Otherwise move down the tree:
           - left if key is smaller
           - right if key is larger
        4. Insert where you find an empty position.
        5. Ignore duplicates.
        """
        new_node = self._new_node(key)

        if self._root is None:
            self._root = new_node
            self._size += 1
            return

        current = self._root
        while True:
            if key < current.val:
                if current.left is None:
                    current.left = new_node
                    self._size += 1
                    return
                current = current.left
            elif key > current.val:
                if current.right is None:
                    current.right = new_node
                    self._size += 1
                    return
                current = current.right
            else:
                # Ignore duplicates.
                return

    def contains(self, key: int) -> bool:
        """Pseudocode:
        1. Search for key using find.
        2. Return whether a result exists.
        """
        return self.find(key) is not None

    def find(self, key: int) -> "Node | None":
        """Pseudocode:
        1. Start at the root.
        2. Compare key with the current node value.
        3. Move left/right according to the BST rule.
        4. Return the node on match.
        5. Return None if key is not found.
        """
        current = self._root
        while current is not None:
            if key == current.val:
                return current
            if key < current.val:
                current = current.left
            else:
                current = current.right
        return None

    def min_value(self) -> "int | None":
        """Pseudocode:
        1. If the tree is empty, return None.
        2. Start at the root.
        3. Move as far left as possible.
        4. Return the value in the final node.
        """
        if self._root is None:
            return None

        current = self._root
        while current.left is not None:
            current = current.left
        return current.val

    def max_value(self) -> "int | None":
        """Pseudocode:
        1. If the tree is empty, return None.
        2. Start at the root.
        3. Move as far right as possible.
        4. Return the value in the final node.
        """
        if self._root is None:
            return None

        current = self._root
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, key: int) -> bool:
        """Pseudocode:
        1. Find the node with key and its parent.
        2. If not found, return False.
        3. If the node has two children:
           - find inorder successor (smallest in right subtree)
           - copy successor value into the node
           - delete successor instead
        4. Link parent to the node's single child (or None).
        5. Return True.
        """
        parent: "Node | None" = None
        current = self._root

        while current is not None and current.val != key:
            parent = current
            if key < current.val:
                current = current.left
            else:
                current = current.right

        if current is None:
            return False

        # If node has two children, replace value with successor and delete successor.
        if current.left is not None and current.right is not None:
            successor_parent = current
            successor = current.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            current.val = successor.val
            parent = successor_parent
            current = successor

        # Node has at most one child.
        child = current.left if current.left is not None else current.right

        if parent is None:
            self._root = child
        elif parent.left == current:
            parent.left = child
        else:
            parent.right = child

        self._size -= 1
        return True

    def height(self) -> int:
        """Pseudocode:
        1. If the tree is empty, return -1.
        2. Use level-order traversal with a queue.
        3. For each level, increase height by 1.
        4. Return height after all nodes are processed.
        """
        if self._root is None:
            return -1

        height = -1
        queue = deque([self._root])

        while queue:
            level_size = len(queue)
            height += 1

            for _ in range(level_size):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return height

    # Classic recursive traversals.
    def inorder(self) -> list[int]:
        """Pseudocode (recursive):
        1. Visit left subtree.
        2. Visit node.
        3. Visit right subtree.
        """
        result: list[int] = []

        def _inorder(node: "Node | None") -> None:
            if node is None:
                return
            _inorder(node.left)
            result.append(node.val)
            _inorder(node.right)

        _inorder(self._root)
        return result

    def preorder(self) -> list[int]:
        """Pseudocode (recursive):
        1. Visit node.
        2. Visit left subtree.
        3. Visit right subtree.
        """
        result: list[int] = []

        def _preorder(node: "Node | None") -> None:
            if node is None:
                return
            result.append(node.val)
            _preorder(node.left)
            _preorder(node.right)

        _preorder(self._root)
        return result

    def postorder(self) -> list[int]:
        """Pseudocode (recursive):
        1. Visit left subtree.
        2. Visit right subtree.
        3. Visit node.
        """
        result: list[int] = []

        def _postorder(node: "Node | None") -> None:
            if node is None:
                return
            _postorder(node.left)
            _postorder(node.right)
            result.append(node.val)

        _postorder(self._root)
        return result

    def level_order(self) -> list[int]:
        """Pseudocode:
        1. If tree is empty, return empty list.
        2. Put root in a queue.
        3. Remove first node and store its value.
        4. Add left and right children to the queue.
        5. Repeat until queue is empty.
        """
        if self._root is None:
            return []

        result: list[int] = []
        queue = deque([self._root])

        while queue:
            node = queue.popleft()
            result.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return result


def run_client_demo() -> None:
    """Pseudocode:
    1. Create a BST.
    2. Insert a small dataset.
    3. Print traversals and basic info.
    4. Test search and deletion.
    5. Print tree after deletion.
    """
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]

    print("Building tree with:", values)
    for value in values:
        bst.insert(value)

    print("Inorder:", bst.inorder())
    print("Preorder:", bst.preorder())
    print("Postorder:", bst.postorder())
    print("Level order:", bst.level_order())
    print("Size:", len(bst))
    print("Min:", bst.min_value(), "Max:", bst.max_value(), "Height:", bst.height())

    key = 40
    print(f"Contains {key}?", bst.contains(key))

    delete_key = 30
    print(f"Deleting {delete_key}:", bst.delete(delete_key))
    print("Inorder after deletion:", bst.inorder())
    print("Size after deletion:", len(bst))


if __name__ == "__main__":
    run_client_demo()