def prod_of_array_except_self(arr):
    total_product = 1
    for element in arr:
        total_product *= element
    i = 0
    while i < len(arr):
        arr[i] = total_product // arr[i]
        i += 1
    return arr


def prod_of_array_except_self_v1(arr):
    n = len(arr)
    left_products = [1 for i in range(n)]
    right_products = [1 for i in range(n)]
    output_arr = []

    for i in range(1, n):
        left_products[i] = arr[i - 1] * left_products[i - 1]

    for i in range(n - 2, -1, -1):
        right_products[i] = arr[i + 1] * right_products[i + 1]

    for i in range(0, n):
        output_arr.append(left_products[i] * right_products[i])

    return output_arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(prod_of_array_except_self(arr))

    arr = [8, 1, 9, 2, 7]
    print(prod_of_array_except_self(arr))

    arr = [1, 2, 3, 4]
    print(prod_of_array_except_self_v1(arr))

    arr = [8, 1, 9, 2, 7]
    print(prod_of_array_except_self_v1(arr))
