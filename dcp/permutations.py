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
        print(toString(a))
    else:
        for i in range(left, right + 1):
            a[left], a[i] = a[i], a[left]
            permute(a, left + 1, right)
            a[left], a[i] = a[i], a[left]  # backtrack


# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

        # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

        # Find the permutations for lst if there are
    # more than 1 characters

    left = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1 :]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            left.append([m] + p)
    return left


# Driver program to test above function


if __name__ == "__main__":
    # Driver program to test the above function
    string = "ABC"
    n = len(string)
    a = list(string)
    permute(a, 0, n - 1)

    # iterative
    data = list("ABC")
    for p in permutation(data):
        print("".join(p))
