from dcp.recursion.subset_sum import subset_sum


def equal_sum(arr, n, sum):
    if sum % 2 != 0:
        return False
    return subset_sum(arr, n, sum/2)


if __name__ == "__main__":
    arr = [5, 1, 5, 11]
    n = 4
    sum = 22
    print(equal_sum(arr, n, sum))