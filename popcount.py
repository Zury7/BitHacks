# Problem: Count number of 1s in binary representation (population count)

# General method: convert to binary string and count '1's
def population_count_general(n):
    return bin(n).count('1')

# Bit hack method: clear lowest 1 until zero
def population_count_bitwise(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

# Example usage
n = 0b1101101
print("General:", population_count_general(n))
print("Bit Hack:", population_count_bitwise(n))
