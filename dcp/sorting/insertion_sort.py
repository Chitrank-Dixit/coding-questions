# python code for insertion sort
class InsertionSort:
    def insertion_sort(self, lis):
        for j in range(1, len(lis)):
            key = lis[j]
            i = j - 1
            while i >= 0 and lis[i] > key:  # corrected the pseudocode i>=0
                lis[i + 1] = lis[i]
                i = i - 1
            lis[i + 1] = key
        return lis


if __name__ == "__main__":
    li = [6, 5, 4, 3, 2, 1]
    Insort = InsertionSort()
    na = Insort.insertion_sort(li)
    print("The sorted list is: ", na)

    li = [1, 5, 7, 4, 8, 2, 6, 5, 4, 3, 2, 1]
    Insort = InsertionSort()
    na = Insort.insertion_sort(li)
    print("The sorted list is: ", na)
