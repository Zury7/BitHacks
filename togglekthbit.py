# Problem: Toggle the k-th bit of an integer 'n'

# General method: convert to bits and toggle manually
def toggle_kth_bit_general(n, k):
    bits = list(bin(n)[2:].zfill(k+1))
    bits[-1 - k] = '0' if bits[-1 - k] == '1' else '1'
    return int(''.join(bits), 2)

# Bit hack method
def toggle_kth_bit_bitwise(n, k):
    return n ^ (1 << k)

# Example usage
n = 10  # 1010
k = 1
print("General:", bin(toggle_kth_bit_general(n, k)))
print("Bit Hack:", bin(toggle_kth_bit_bitwise(n, k)))
