# Problem: Find log2(n) assuming n is a power of 2

# General method: count shifts
def log2_general(n):
    count = 0
    while n > 1:
        n >>= 1
        count += 1
    return count

# Bit hack method: using bit_length()
def log2_bitwise(n):
    return n.bit_length() - 1

# Example usage
n = 8
print("General:", log2_general(n))
print("Bit Hack:", log2_bitwise(n))
