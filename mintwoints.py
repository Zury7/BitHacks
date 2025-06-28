# Problem: Find minimum of two integers

# General method: standard comparison
def min_with_branch(a, b):
    return a if a < b else b

# Bit hack method: no branching
def min_no_branch(a, b):
    return b ^ ((a ^ b) & -(a < b))

# Example usage
a, b = 5, 9
print("General:", min_with_branch(a, b))
print("Bit Hack:", min_no_branch(a, b))
