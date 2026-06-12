# file: ex_21_02_parent_ref_start.py
# Dette er en startkode for øving 21.2: Binært tre med parent-referanser.

# Importen under sørger for å utsette typevaluering,
# undertykker forstyrrende feil 
from __future__ import annotations
from collections import deque

class Node:
    def __init__(self, key: int):
        """Lagrer venstre/høyre barn og nodeverdi."""
        # Typehint: "Node | None" leses som "enten en Node eller None".
        self.left: Node | None = None
        self.right: Node | None = None
        # TODO 1: Legg til parent-referanseattributt i Node.
        # Eksempel: self.parent: Node | None = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        """Starter med et tomt tre (ingen rot, storrelse 0)."""
        self._root: Node | None = None
        self._size = 0

    def __len__(self) -> int:
        """Returnerer antall noder i treet."""
        return self._size

    def is_empty(self) -> bool:
        """Returnerer True nar treet er tomt."""
        return self._root is None

    def _new_node(self, key: int) -> Node:
        """Node-fabrikk: kan overstyres i subklasser."""
        return Node(key)

    def insert(self, key: int) -> None:
        """TODO 2:
        Sett inn key etter BST-regelen:
        - gå til venstre hvis key er mindre
        - gå til høyre hvis key er større
        - ignorer duplikater

        Oppdater parent-referanser når en ny node kobles inn
        (bruk new_node.parent = current).
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
                    # TODO: sett parent-referansen i new_node til current
                    self._size += 1
                    return
                current = current.left
            elif key > current.val:
                if current.right is None:
                    current.right = new_node
                    # TODO: sett parent-referansen i new_node til current
                    self._size += 1
                    return
                current = current.right
            else:
                return

    def contains(self, key: int) -> bool:
        """Sjekker om key finnes ved a bruke find()."""
        return self.find(key) is not None

    def find(self, key: int) -> Node | None:
        """Søker etter key og returnerer noden, eller None hvis ikke funnet."""
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
        """TODO 3:
        Returner True hvis noden med key finnes og er en løvnode.
        """
        raise NotImplementedError

    def get_path(self, key: int) -> list[int]:
        # Typehint: "list[int]" betyr en liste som skal inneholde heltall.
        """TODO 4:
        Returner en liste med verdier fra noden med key opp til rota.
        Bruk parent-referanser.
        Eksempel: hvis stien er 40 -> 30 -> 50, returner [40, 30, 50].
        """
        raise NotImplementedError

    def min_value(self) -> int | None:
        # Typehint: "int | None" betyr at resultatet er et heltall eller None.
        """Returnerer minste verdi i treet, eller None hvis tomt."""
        if self._root is None:
            return None

        current = self._root
        while current.left is not None:
            current = current.left
        return current.val

    def max_value(self) -> int | None:
        """Returnerer største verdi i treet, eller None hvis tomt."""
        if self._root is None:
            return None

        current = self._root
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, key: int) -> bool:
        """TODO 5:
        Slett noden med key:
        - finn noden og forelderen
        - ved to barn: bruk inorder-successor
        - koble inn barn (eller None) der noden stod

        Oppdater parent-referanser slik at de forblir korrekte
        etter omkobling av noder.
        """
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
            # TODO: hvis child finnes, skal child.parent bli None
        elif parent.left == current:
            parent.left = child
            # TODO: hvis child finnes, skal child.parent bli parent
        else:
            parent.right = child
            # TODO: hvis child finnes, skal child.parent bli parent

        self._size -= 1
        return True

    def height(self) -> int:
        """Returnerer høyde med level-order traversering (-1 for tomt tre)."""
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
        """Traversering: venstre, node, hoyre."""
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
        """Traversering: node, venstre, hoyre."""
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
        """Traversering: venstre, hoyre, node."""
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
        """Traverserer nivaa for nivaa med queue."""
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
    """Lager et eksempeltre og skriver ut enkel status."""
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        bst.insert(value)

    print("Inorder:", bst.inorder())
    print("Size:", len(bst))

    # Grunnsjekker som skal virke for startkode uten TODO-implementasjon.
    print("Contains 40?", bst.contains(40))
    print("Contains 99?", bst.contains(99))
    print("Find 60?", bst.find(60) is not None)
    print("Find 99?", bst.find(99) is not None)
    print("Min/Max:", bst.min_value(), bst.max_value())
    print("Grunnsjekker: ferdig")

    # Eksempelkall etter at TODO-punktene er implementert:
    try:
        min_key = bst.min_value()
        max_key = bst.max_value()
        root_key = values[0]

        if min_key is not None:
            min_node = bst.find(min_key)
            if min_node is not None:
                print(f"Leaf min ({min_key})?", bst.is_leaf(min_node.val))

        if max_key is not None:
            max_node = bst.find(max_key)
            if max_node is not None:
                print(f"Leaf max ({max_key})?", bst.is_leaf(max_node.val))

        print(f"Leaf root ({root_key})?", bst.is_leaf(root_key))
        print("Path from 40 to root:", bst.get_path(40))
        print("TODO-sjekker: OK")
    except NotImplementedError:
        print("TODO-sjekker: hoppet over (metoder ikke implementert enda).")


if __name__ == "__main__":
    run_client_demo()
