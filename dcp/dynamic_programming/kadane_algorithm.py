from sys import maxsize


# Function to find the maximum contiguous subarray
# and print its starting and end index
def maxSubArraySum(a, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    print("Maximum contiguous sum is %d" % (max_so_far))
    print("Starting Index %d" % (start))
    print("Ending Index %d" % (end))


def kadane_algo(arr):
    curr_sum = 0
    max_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0
    return max_sum

# on negative numbers
def kadane_algorithm(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    # Driver program to test maxSubArraySum
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    maxSubArraySum(a, len(a))

    a = [-2, -3, -4, -1, -2, -1, -5, -3]
    maxSubArraySum(a, len(a))


    a = [5, -4, -2, 6, -1]
    print(kadane_algo(a))

    a = [-5, -4, -2, -6, -1]
    print(kadane_algo(a))

    arr = [-2, -3, -4, -1, -2, -1, -5, -3]
    max_subarray_sum = kadane_algorithm(arr)
    print(max_subarray_sum)