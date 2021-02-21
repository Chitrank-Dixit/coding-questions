# implementing selection sort algorithm
def selection_sort(x):
    temp = 0
    for i in range(0, len(x)):
        j = i
        for k in range(i + 1, len(x)):
            if x[k] < x[j]:
                j = k
        temp = x[i]
        x[i] = x[j]
        x[j] = temp
    return x


if __name__ == "__main__":
    lis = [6, 5, 4, 3, 2, 1]
    sor_lis = selection_sort(lis)
    print("Sorted list is: ", sor_lis)
