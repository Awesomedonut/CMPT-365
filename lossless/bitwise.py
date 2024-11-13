x = 0b000
x = x << 2
print("3 " + str(bin(x)))

newbits = 0b10

x = x | newbits
print("8 " + str(bin(x)))

x = x & 0b111
print("11 " + str(bin(x)))

print("#############")

x = x << 3
print("16 " + str(bin(x)))

newbits = 0b000

x = x | newbits
print("21 " + str(bin(x)))

x = x & 0b111
print("24 " + str(bin(x)))

print(bin(0b00010 & 0b111))