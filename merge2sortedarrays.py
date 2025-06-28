# Problem: Merge two sorted arrays into one sorted array

# General method: standard two-pointer merge
def merge_sorted_general(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

# Bit hack: Not applicable; this is a comparison-based algorithm

# Example usage
a = [1, 3, 5]
b = [2, 4, 6]
print("Merged:", merge_sorted_general(a, b))
