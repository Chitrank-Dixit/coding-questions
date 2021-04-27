from sys import maxsize


def maxSubArraySum(a, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


def maxSubArraySum_v1(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


def maxSubArraySum_v2(a, size):
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


def maxSubArraySum_v3(a, size):
    max_so_far = a[0]
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only
        # when  max_ending_here > 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far


if __name__ == "__main__":
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    print("Maximum contiguous sum is 1", maxSubArraySum(a, len(a)))

    print("Maximum contiguous sum is 2", maxSubArraySum_v1(a, len(a)))

    print("Maximum contiguous sum is 3", maxSubArraySum_v2(a, len(a)))

    print("Maximum contiguous sum is 4", maxSubArraySum_v3(a, len(a)))
