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

class BitReader:
    def __init__(self, bitstring):
        self.bitstring = bitstring
        self.position = 0
    
    def read_bits(self, num_bits):
        if self.position + num_bits > len(self.bitstring):
            return None
        bits = self.bitstring[self.position:self.position + num_bits]
        self.position += num_bits
        return int(bits, 2)

def huffman_decode(input_bits):
    reader = BitReader(input_bits)
    x = reader.read_bits(3)
    decoded_symbols = []
    k = 0

    while x is not None:
        symbol = HuffDec[x][0]
        length = HuffDec[x][1]
        newbits = reader.read_bits(length)
        
        print(f"Round {k}:")
        print(f"  k: {k}")
        print(f"  symbol: {symbol}")
        print(f"  length: {length}")
        print(f"  newbits: {bin(newbits)[2:]:0>{length}}" if newbits is not None else "  newbits: None")
        print(f"  x before shift: {bin(x)[2:]:0>3}")
        
        if newbits is None:
            break
            
        decoded_symbols.append(symbol)
        
        x = ((x << length) | newbits) & 0b111
        print(f"  x after operations: {bin(x)[2:]:0>3}\n")
        k += 1

    return decoded_symbols

input_bitstring = "0001000011011"
decoded_output = huffman_decode(input_bitstring)
print("Decoded symbols:", decoded_output)
