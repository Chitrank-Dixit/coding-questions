def maximum(arr):
    maxi = 0
    for element in arr:
        if element > maxi:
            maxi = element
    return maxi


if __name__ == "__main__":
    print(maximum([1, 5, 2, 4, 9, 12]))
