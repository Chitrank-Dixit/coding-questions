# python program for above approach

# function sets the values of
# x and *y to non-repeating elements
# in an array arr[] of size n
def get2NonRepeatingNos(nums, n):
    nums.sort()

    ans = []

    i = 0
    while (i < n - 1):
        if (nums[i] != nums[i + 1]):
            ans.append(nums[i])
            i = i + 1
        else:
            i = i + 2

    if (len(arr) == 1):
        ans.append(nums[n - 1])

    return ans


# Function to find two non-repeating numbers in an array
def get_2_non_repeating_nos(nums):
    # Pass 1:
    # Get the XOR of the two numbers we need to find
    diff = 0
    for num in nums:
        diff ^= num

    # Get its last set bit
    diff &= -diff

    # Pass 2:
    rets = [0, 0]  # this list stores the two numbers we will return
    for num in nums:
        if (num & diff) == 0:  # the bit is not set
            rets[0] ^= num
        else:  # the bit is set
            rets[1] ^= num

    # Ensure the order of the returned numbers is consistent
    if rets[0] > rets[1]:
        rets[0], rets[1] = rets[1], rets[0]

    return rets


if __name__ == '__main__':
    # Driver code
    arr = [2, 3, 7, 9, 11, 2, 3, 11]
    n = len(arr)
    ans = get2NonRepeatingNos(arr, n)
    print("The non-repeating elements are ", ans[0], " and ", ans[1])

    arr = [2, 3, 7, 9, 11, 2, 3, 11]
    result = get_2_non_repeating_nos(arr)
    print("The non-repeating elements are", result[0], "and", result[1])

