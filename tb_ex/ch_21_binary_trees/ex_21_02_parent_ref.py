# file: ex_21_02_parent_ref.py
# Solution to exercise 21.2: Binary tree with parent references.
from __future__ import annotations
from collections import deque


class Node:
	def __init__(self, key: int):
		self.left: Node | None = None
		self.right: Node | None = None
		# Parent is kept as a direct reference to simplify upward traversal.
		self.parent: Node | None = None
		self.val = key


class BinarySearchTree:
	def __init__(self):
		self._root: Node | None = None
		self._size = 0

	def __len__(self) -> int:
		return self._size

	def is_empty(self) -> bool:
		return self._root is None

	def _new_node(self, key: int) -> Node:
		return Node(key)

	def insert(self, key: int) -> None:
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
					# Maintain parent link when attaching a new left child.
					new_node.parent = current
					self._size += 1
					return
				current = current.left
			elif key > current.val:
				if current.right is None:
					current.right = new_node
					# Maintain parent link when attaching a new right child.
					new_node.parent = current
					self._size += 1
					return
				current = current.right
			else:
				return

	def contains(self, key: int) -> bool:
		return self.find(key) is not None

	def find(self, key: int) -> Node | None:
		# Return the node object itself (not only True/False).
		current = self._root
		while current is not None:
			if key == current.val:
				return current
			if key < current.val:
				current = current.left
			else:
				current = current.right
		return None

	def is_leaf(self, key: int) -> bool:
		# A leaf node has no left and no right child.
		node = self.find(key)
		if node is None:
			return False
		return node.left is None and node.right is None

	def get_path(self, key: int) -> list[int]:
		# Build path from the found node up to the root using parent links.
		node = self.find(key)
		if node is None:
			return []

		path: list[int] = []
		current = node
		while current is not None:
			path.append(current.val)
			current = current.parent
		return path

	def min_value(self) -> int | None:
		if self._root is None:
			return None

		current = self._root
		while current.left is not None:
			current = current.left
		return current.val

	def max_value(self) -> int | None:
		if self._root is None:
			return None

		current = self._root
		while current.right is not None:
			current = current.right
		return current.val

	def delete(self, key: int) -> bool:
		parent: Node | None = None
		current = self._root

		while current is not None and current.val != key:
			parent = current
			if key < current.val:
				current = current.left
			else:
				current = current.right

		if current is None:
			return False

		if current.left is not None and current.right is not None:
			successor_parent = current
			successor = current.right
			while successor.left is not None:
				successor_parent = successor
				successor = successor.left

			current.val = successor.val
			parent = successor_parent
			current = successor

		child = current.left if current.left is not None else current.right

		if parent is None:
			self._root = child
			if child is not None:
				# New root must have no parent.
				child.parent = None
		elif parent.left == current:
			parent.left = child
			if child is not None:
				# Reconnect parent link after delete in left branch.
				child.parent = parent
		else:
			parent.right = child
			if child is not None:
				# Reconnect parent link after delete in right branch.
				child.parent = parent

		self._size -= 1
		return True

	def height(self) -> int:
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

	def inorder(self) -> list[int]:
		result: list[int] = []

		def _inorder(node: Node | None) -> None:
			if node is None:
				return
			_inorder(node.left)
			result.append(node.val)
			_inorder(node.right)

		_inorder(self._root)
		return result

	def preorder(self) -> list[int]:
		result: list[int] = []

		def _preorder(node: Node | None) -> None:
			if node is None:
				return
			result.append(node.val)
			_preorder(node.left)
			_preorder(node.right)

		_preorder(self._root)
		return result

	def postorder(self) -> list[int]:
		result: list[int] = []

		def _postorder(node: Node | None) -> None:
			if node is None:
				return
			_postorder(node.left)
			_postorder(node.right)
			result.append(node.val)

		_postorder(self._root)
		return result

	def level_order(self) -> list[int]:
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
	bst = BinarySearchTree()
	values = [50, 30, 70, 20, 40, 60, 80]

	for value in values:
		bst.insert(value)

	print("Inorder:", bst.inorder())
	print("Size:", len(bst))
	min_key = bst.min_value()
	max_key = bst.max_value()

	if min_key is not None:
		print("Minimum verdi ligger helt til venstre og må være en løvnode", bst.is_leaf(min_key))
	if max_key is not None:
		print("Max verdi ligger helt til høyre og må være en løvnode", bst.is_leaf(max_key))
	print("Path from 40 to root:", bst.get_path(40))
	print("Path from 999 to root:", bst.get_path(999))

	root_key = values[0]

	print(f"Er root en løvnode ({root_key})?", bst.is_leaf(root_key))

	print("Delete 20:", bst.delete(20), "Contains 20:", bst.contains(20))
	print("Delete 30:", bst.delete(30), "Contains 30:", bst.contains(30))
	print("Size after deletes:", len(bst))


if __name__ == "__main__":
	run_client_demo()
