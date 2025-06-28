# Problem: Extract 'length' bits from integer 'n' starting at position 'pos'

# General method: convert to binary string and slice
def extract_bit_field_general(n, pos, length):
    return int(bin(n)[2:].zfill(pos + length)[-1 - pos - length + 1: -pos if pos != 0 else None], 2)

# Bit hack method
def extract_bit_field_bitwise(n, pos, length):
    mask = (1 << length) - 1
    return (n >> pos) & mask

# Example usage
n = 0b11010110
pos = 2
length = 3
print("General:", bin(extract_bit_field_general(n, pos, length)))
print("Bit Hack:", bin(extract_bit_field_bitwise(n, pos, length)))
