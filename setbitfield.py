# Problem: Set a bit field in 'n' starting at position 'pos' to 'val' (length bits)

# General method: using binary string manipulation
def set_bit_field_general(n, pos, length, val):
    bits = list(bin(n)[2:].zfill(pos + length))
    val_bits = bin(val)[2:].zfill(length)
    bits[-1 - pos - length + 1 : -pos if pos != 0 else None] = list(val_bits)
    return int(''.join(bits), 2)

# Bit hack method
def set_bit_field_bitwise(n, pos, length, val):
    mask = ((1 << length) - 1) << pos
    n_cleared = n & ~mask
    val_shifted = (val << pos) & mask
    return n_cleared | val_shifted

# Example usage
n = 0b10101100
pos = 2
length = 3
val = 0b101
print("General:", bin(set_bit_field_general(n, pos, length, val)))
print("Bit Hack:", bin(set_bit_field_bitwise(n, pos, length, val)))
