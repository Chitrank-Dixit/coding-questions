from stack import Stack


def next_greater(arr):
    s = Stack()
    s.top = -1
    i = len(arr) - 1
    arr1 = [0 for i in range(len(arr))]
    while i >= 0:
        # checking if the current value is greater than the value at the top of stack
        # if it is then we remove it from the stack
        while not s.is_empty() and s.tos() <= arr[i]:
            s.pop()

        if s.is_empty():
            arr1[i] = -1
        else:
            arr1[i] = s.tos()
        s.push(arr[i])

        i -= 1

    for j in range(len(arr)):
        print(f"{arr[j]} ---> {arr1[j]}")


if __name__ == "__main__":
    arr = [4, 5, 2, 25]
    print(next_greater(arr))
