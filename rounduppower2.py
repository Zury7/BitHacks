# Problem: Round up an integer to the next power of 2

# General method: multiply powers until we pass n
def round_up_power2_general(n):
    if n <= 1:
        return 1
    power = 1
    while power < n:
        power *= 2
    return power

# Bit hack method
def round_up_power2_bitwise(n):
    if n <= 1:
        return 1
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return n + 1

# Example usage
n = 20
print("General:", round_up_power2_general(n))
print("Bit Hack:", round_up_power2_bitwise(n))
