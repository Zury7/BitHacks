# Problem: Get the least significant 1 bit of a number

# General method: loop through bits
def least_significant_one_general(n):
    for i in range(n.bit_length()):
        if n & (1 << i):
            return 1 << i
    return 0

# Bit hack method
def least_significant_one_bitwise(n):
    return n & -n

# Example usage
n = 0b101100
print("General:", bin(least_significant_one_general(n)))
print("Bit Hack:", bin(least_significant_one_bitwise(n)))
