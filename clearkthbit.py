# Problem: Clear the k-th bit of an integer 'n'

# General method: convert to list of bits and clear
def clear_kth_bit_general(n, k):
    bits = list(bin(n)[2:].zfill(k+1))
    bits[-1 - k] = '0'
    return int(''.join(bits), 2)

# Bit hack method
def clear_kth_bit_bitwise(n, k):
    return n & ~(1 << k)

# Example usage
n = 10  # 1010
k = 1
print("General:", bin(clear_kth_bit_general(n, k)))
print("Bit Hack:", bin(clear_kth_bit_bitwise(n, k)))
