# Define the Huffman decoding table
HuffDec = [
    ('a', 2),
    ('a', 2),
    ('b', 3),
    ('c', 3),
    ('d', 1),
    ('d', 1),
    ('d', 1),
    ('d', 1)
]

def read_bits(num_bits):
    # Replace this with actual bit reading logic
    # For demonstration, we'll use a placeholder that returns a sequence of bits
    return int(input(f"Enter {num_bits} bits as a binary string: "), 2)

def huffman_decode():
    x = read_bits(3)
    k = 0
    decoded_symbols = []

    while True:  # Replace with EOF condition if reading from a file/stream
        symbol = HuffDec[x][0]
        decoded_symbols.append(symbol)
        k += 1

        length = HuffDec[x][1]
        x = x << length  # Shift left by the symbol length
        newbits = read_bits(length)  # Read 'length' number of new bits
        x = x | newbits  # Combine the old bits with new bits
        x = x & 0b111  # Ensure x stays within 3 bits (111 in binary is 7)

        # Break condition or EOF should be placed here based on input source
        # For demonstration, we'll break after a certain number of symbols
        if k >= 10:  # For example, stop after decoding 10 symbols
            break

    return decoded_symbols

# Run the Huffman decoder
decoded_output = huffman_decode()
print("Decoded symbols:", decoded_output)
