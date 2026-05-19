# file: sc_21_03_huffman_coding_using_heapq.py

import heapq

ASCII_RANGE = 128

def main():
    text = input("Enter a text: ").strip()
    if not text:
        print("Please enter at least one ASCII character.")
        return

    if any(ord(char) >= ASCII_RANGE for char in text):
        print("This example supports ASCII characters only.")
        return
    
    counts = get_character_frequency(text)  # Count each ASCII character.

    print(f"{'ASCII Code':<14s} {'Character':<14s}",
          f"{'Frequency':<14s} {'Code':<14s}")  
    
    huffman_root = get_huffman_tree(counts)  # Build the Huffman tree.
    codes = get_code(huffman_root)  # Derive the bit code for each leaf.
        
    for i in range(len(codes)):
        # Only print characters that appeared in the input text.
        if counts[i] != 0:
            print(f"{i:<14d} {chr(i):<14s}",
                  f"{counts[i]:<14d} {codes[i]:<14s}")
 

# Get Huffman codes for the characters 
# This method is called once after a Huffman tree is built
def get_code(current: "Node") -> list[str]:
    codes = ASCII_RANGE * [""]  # Stores the code for each ASCII character.

    # A one-character input produces a one-node tree.
    if current.left is None and current.right is None:
        assert current.element is not None
        codes[ord(current.element)] = "0"
        return codes

    assign_code(current, codes)
    return codes
  
# Recursively get codes to the leaf node 
def assign_code(current: "Node", codes: list[str]) -> None:
    if current.left is not None:
        # By convention, going left adds 0 and going right adds 1.
        current.left.code = current.code + "0"
        assign_code(current.left, codes)

        assert current.right is not None
        current.right.code = current.code + "1"
        assign_code(current.right, codes)
    else:
        # A leaf node contains a real character, so store its full code.
        assert current.element is not None
        codes[ord(current.element)] = current.code
  
# Get a Huffman tree from the codes   
def get_huffman_tree(counts: list[int]) -> "Node":
    # Each heap entry starts as a one-node tree for one character.
    heap: list[tuple[int, Node]] = [] # weight and the tree node
    for i in range(len(counts)):
        if counts[i] > 0:
            heapq.heappush(heap, (counts[i], Node(counts[i], chr(i))))
    
    while len(heap) > 1:
        # Merge the two smallest trees into one larger tree.
        weight1, left = heapq.heappop(heap) # left is the smaller tree
        weight2, right = heapq.heappop(heap) # right is the larger tree
        new_node = Node(weight1 + weight2)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, (new_node.weight, new_node))

    return heapq.heappop(heap)[1]  # The last remaining tree is the root.
  
# Get the frequency of the characters 
def get_character_frequency(text: str) -> list[int]:
    counts = ASCII_RANGE * [0]
    
    for char in text:
        counts[ord(char)] += 1
    
    return counts
  
# Define a Huffman coding tree node
class Node:
    # Create a node with the specified weight and character 
    def __init__(self, weight: int, element: str | None = None):
        self.weight = weight # The total frequency of the characters in this subtree.
        self.element = element # A character for leaf nodes, None for internal nodes.
        self.left: Node | None = None # could be Node or None
        self.right: Node | None = None
        self.code = "" # Bit code for the path from the root to this node

    # Overload the comparison operators for heapq
    def __lt__(self, other: "Node") -> bool:
        return self.weight < other.weight

if __name__ == "__main__":
    main()