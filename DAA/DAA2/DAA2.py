class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def calculate_frequency(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

def build_huffman_tree(frequency):
    nodes = [Node(char, freq) for char, freq in frequency.items()]

    while len(nodes) > 1:
        # Sort nodes by frequency
        nodes.sort(key=lambda x: x.freq)

        # Take two nodes with the smallest frequency
        left = nodes.pop(0)
        right = nodes.pop(0)

        # Create a new internal node with these two nodes as children
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add the new node back to the list
        nodes.append(merged)

    return nodes[0]  # The root of the Huffman tree

def generate_codes(node, prefix='', codebook={}):
    if node is not None:
        if node.char is not None:  # Leaf node
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + '0', codebook)
        generate_codes(node.right, prefix + '1', codebook)
    return codebook

def huffman_encoding(text):
    frequency = calculate_frequency(text)
    huffman_tree = build_huffman_tree(frequency)
    huffman_codes = generate_codes(huffman_tree)
    return huffman_codes

def main():
    text = input("Enter a string to encode: ")
    huffman_codes = huffman_encoding(text)

    print("\nHuffman Codes:")
    for char, code in huffman_codes.items():
        print(f"'{char}': {code}")

    # Encoding the input string
    encoded_string = ''.join(huffman_codes[char] for char in text)
    print(f"\nEncoded String: {encoded_string}")

if __name__ == "__main__":
    main()
