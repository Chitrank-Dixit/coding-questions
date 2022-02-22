# implemeting bubble sort in Python
def bubble_sort(sort):
    temp = 0
    for i in range(0, len(sort)):
        for j in range(
            len(sort) - 1, i, -1
        ):  # here I have used reverse range range(para1,para2,para3)
            if sort[j] < sort[j - 1]:
                temp = sort[j]
                sort[j] = sort[j - 1]
                sort[j - 1] = temp
    return sort


def bubble_sort_v1(sort):
    temp = 0
    for i in range(0, len(sort)):
        is_swapped = False
        for j in range(
            len(sort) - 1, i, -1
        ):  # here I have used reverse range range(para1,para2,para3)
            if sort[j] < sort[j - 1]:
                temp = sort[j]
                sort[j] = sort[j - 1]
                sort[j - 1] = temp
                is_swapped = True
        if not is_swapped:
            break
    return sort


if __name__ == "__main__":
    to_sort = [6, 5, 4, 3, 2, 1]
    sorted_list = bubble_sort(to_sort)
    print("Sorted list is: ", sorted_list)

    to_sort = [6, 5, 4, 3, 2, 1]
    sorted_list = bubble_sort_v1(to_sort)
    print("Sorted list is: ", sorted_list)