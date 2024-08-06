def reverse_array_using_stack(arr):
    stack = []

    # Push elements onto the stack
    for element in arr:
        stack.append(element)

    # Pop elements from the stack to reverse the array
    for i in range(len(arr)):
        arr[i] = stack.pop()


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    reverse_array_using_stack(arr)
    print("Reversed Array:", arr)
