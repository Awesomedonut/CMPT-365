def huffman_decoding():
    x = ReadBits(3)
    k = 0
    while (not EOF) { 
        symbol[k++] = HuffDec[x][0]
        length = HuffDec[x][1]
        x = x << length
        newbits = ReadBits(length)
        x = x | newbits
        x = x & 111B
    }