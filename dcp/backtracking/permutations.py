# Python program to print all permutations with
# duplicates allowed


def toString(List):
    return "".join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, left, right):
    if left == right:
        return toString(a)
    else:
        permutation_list = []
        for i in range(left, right + 1):
            a[left], a[i] = a[i], a[left]
            permutations = permute(a, left + 1, right)  # recursion
            permutation_list.append(permutations)
            a[left], a[i] = a[i], a[left]  # backtrack

    return permutation_list


if __name__ == "__main__":
    # Driver program to test the above function
    string = "ABC"
    n = len(string)
    a = list(string)
    permutations = permute(a, 0, n - 1)
