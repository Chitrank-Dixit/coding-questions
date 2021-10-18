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


def permutation(input_list, used, partial=list()):
    if len(partial) == len(input_list):
        print(partial)
    else:
        for i in range(0, len(input_list)):
            if not used[i] and not (
                input_list[i] == input_list[i - 1] and not used[i - 1]
            ):
                used[i] = True
                partial.append(input_list[i])
                permutation(input_list, partial, used)
                used[i] = False
                partial.pop(len(partial) - 1)


if __name__ == "__main__":
    # Driver program to test the above function
    string = "ABC"
    n = len(string)
    a = list(string)
    permutations = permute(a, 0, n - 1)
    print(permutations)

    list_of_nums = [1, 2, 3, 4]
    used = {index: False for index, num in enumerate(list_of_nums)}
    print(permutation(input_list=list_of_nums, used=used))
