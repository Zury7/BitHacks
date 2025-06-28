# Problem: Set the k-th bit of an integer 'n'

# General method: use list/array of bits
def set_kth_bit_general(n, k):
    bits = list(bin(n)[2:].zfill(k+1))
    bits[-1 - k] = '1'
    return int(''.join(bits), 2)

# Bit hack method
def set_kth_bit_bitwise(n, k):
    return n | (1 << k)

# Example usage
n = 8  # 1000
k = 1
print("General:", bin(set_kth_bit_general(n, k)))
print("Bit Hack:", bin(set_kth_bit_bitwise(n, k)))
