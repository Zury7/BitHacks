# Problem: Compute (a + b) % mod

# General method
def modular_add_general(a, b, mod):
    return (a + b) % mod

# Bit hack method: addition & conditional subtract (if >= mod)
def modular_add_bitwise(a, b, mod):
    res = a + b
    return res if res < mod else res - mod

# Example usage
a, b, mod = 10, 15, 12
print("General:", modular_add_general(a, b, mod))
print("Bit Hack:", modular_add_bitwise(a, b, mod))
