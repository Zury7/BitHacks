# Problem: Swap two integers without using a temporary variable

# General method: use a temporary variable
def swap_general(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Bit hack method: XOR swap
def swap_bitwise(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Example usage
a, b = 5, 9
print("General:", swap_general(a, b))
print("Bit Hack:", swap_bitwise(a, b))
