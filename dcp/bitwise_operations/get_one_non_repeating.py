# Python code to find the array element that appears only once

# Function to find the array
# element that appears only once
def findSingle(A, ar_size):
    # iterate over every element
    for i in range(ar_size):

        # Initialize count to 0
        count = 0
        for j in range(ar_size):

            # Count the frequency
            # of the element
            if (A[i] == A[j]):
                count += 1

        # If the frequency of
        # the element is one
        if (count == 1):
            return A[i]

        # If no element exist
    # at most once
    return -1


# function to find the once
# appearing element in array
def findSinglev1(ar, n):
    res = ar[0]

    # Do XOR of all elements and return
    for i in range(1, n):
        res = res ^ ar[i]

    return res


def singleNumber(nums):
    # applying the formula.
    return 2 * sum(set(nums)) - sum(nums)


def singleelement(arr, n):
    low = 0
    high = n - 2
    mid = 0
    while (low <= high):
        mid = (low + high) // 2
        if (arr[mid] == arr[mid ^ 1]):
            low = mid + 1
        else:
            high = mid - 1

    return arr[low]


def singleelementv1(arr, n):
    # dictionary to store frequency
    mm = {}
    for i in range(n):
        # storing frequency
        if arr[i] in mm:
            mm[arr[i]] += 1
        else:
            mm[arr[i]] = 1

    # iterating over dictionary
    for key, value in mm.items():
        # returning element with frequency 1
        if value == 1:
            return key


if __name__ == "__main__":
    ar = [2, 3, 5, 4, 5, 3, 4]
    n = len(ar)
    # Function call
    print("Element occurring once is", findSingle(ar, n))

    ar = [2, 3, 5, 4, 5, 3, 4]
    print("Element occurring once is", findSinglev1(ar, len(ar)))

    a = [2, 3, 5, 4, 5, 3, 4]
    print(int(singleNumber(a)))

    a = [15, 18, 16, 18, 16, 15, 89]
    print(int(singleNumber(a)))

    arr = [2, 3, 5, 4, 5, 3, 4]
    size = len(arr)
    arr.sort()
    print(singleelement(arr, size))

    arr = [2, 3, 5, 4, 5, 3, 4]
    size = len(arr)
    arr.sort()
    print(singleelementv1(arr, size))


