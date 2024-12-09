from collections import Counter
import heapq

def huffman_encode(img_as_triplet_arr):
    symbol_frequencies = Counter(img_as_triplet_arr)

    symbols = []
    # sort symbols into a list, according to frequency
    # implemented using min heap

    for symbol in symbol_frequencies:
        pixel = [symbol_frequencies[symbol], [symbol, ""]]
        symbols.append(pixel)

    heapq.heapify(symbols)
    
    # build the huffman tree
    while len(symbols) > 1:
        left_node = heapq.heappop(symbols)
        right_node = heapq.heappop(symbols)
        
        for pair in left_node[1:]:
            pair[1] = '0' + pair[1]
        for pair in right_node[1:]:
            pair[1] = '1' + pair[1]
        
        parent_node = [left_node[0] + right_node[0]] + left_node[1:] + right_node[1:]
        heapq.heappush(symbols, parent_node)
    
    # assign huff codes
    huffman_tree = symbols[0]
    huffman_codes = {symbol: code for symbol, code in huffman_tree[1:]}
    
    # encode the original sequence of triplets/symbols
    encoded_arr = ''.join(huffman_codes[symbol] for symbol in img_as_triplet_arr)
    
    return huffman_codes, encoded_arr


# bmp_arr = """95 169 243
# 96 168 243
# 96 168 245
# 96 170 243
# 98 170 247
# 98 172 247
# 99 171 249"""

#huffman, encoded_arr = huffman_coding(bmp_arr)
# print("huffman codes:")
# for symbol, code in huffman.items():
#     print(f"{symbol}: {code}")
# print("\necoded arr:", encoded_arr)

    
   # return huffman_codes, encoded_arr

#bmp_array = [77, 7, 7, 7, 7, 7, 7, 77, 7, 7, 7, 7, 77]
#huffman_codes, encoded_ar = huffman_compress(bmp_array)
# print("huff coes:", huffman_codes)
# print(" array:", encoded_arr)

# symbols = img_as_triplet_arr