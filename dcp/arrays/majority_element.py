"""
Write a function which takes an array and prints the majority element (if it exists), otherwise prints
“No Majority Element”. A majority element in an array A[] of size n is an element that appears more than n/2 times
(and hence there is at most one such element).
"""


def findMajority(arr, n):
    maxCount = 0
    index = -1  # sentinels
    for i in range(n):

        count = 0
        for j in range(n):

            if arr[i] == arr[j]:
                count += 1

        # update maxCount if count of
        # current element is greater
        if count > maxCount:
            maxCount = count
            index = i

    # if maxCount is greater than n/2
    # return the corresponding element
    if maxCount > n // 2:
        print(arr[index])

    else:
        print("No Majority Element")


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1  # count of number of times data is inserted in tree


# class for binary search tree
# it initialises tree with None root
# insert function inserts node as per BST rule
# and also checks for majority element
# if no majority element is found yet, it returns None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data, n):
        out = None
        if self.root is None:
            self.root = Node(data)
        else:
            out = self.insertNode(self.root, data, n)
        return out

    def insertNode(self, currentNode, data, n):
        if currentNode.data == data:
            currentNode.count += 1
            if currentNode.count > n // 2:
                return currentNode.data
            else:
                return None
        elif currentNode.data < data:
            if currentNode.right:
                self.insertNode(currentNode.right, data, n)
            else:
                currentNode.right = Node(data)
        elif currentNode.data > data:
            if currentNode.left:
                self.insertNode(currentNode.left, data, n)
            else:
                currentNode.left = Node(data)


def findCandidate(A):
    maj_index = 0
    count = 1
    for i in range(len(A)):
        if A[maj_index] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return A[maj_index]


# Function to check if the candidate occurs more than n/2 times


def isMajority(A, cand):
    count = 0
    for i in range(len(A)):
        if A[i] == cand:
            count += 1
    if count > len(A) / 2:
        return True
    else:
        return False


# Function to print Majority Element


def printMajority(A):
    # Find the candidate for Majority
    cand = findCandidate(A)

    # Print the candidate if it is Majority
    if isMajority(A, cand):
        print(cand)
    else:
        print("No Majority Element")


if __name__ == "__main__":

    # brute force
    arr = [1, 1, 2, 1, 3, 5, 1]
    n = len(arr)

    # Function calling
    findMajority(arr, n)

    # using binary trees
    arr = [3, 2, 3]
    n = len(arr)

    # declaring None tree
    tree = BST()
    flag = 0
    for i in range(n):
        out = tree.insert(arr[i], n)
        if out is not None:
            print(arr[i])
            flag = 1
            break
    if flag == 0:
        print("No Majority Element")

    # using moore voting algorithm
    A = [1, 3, 3, 1, 2]

    # Function call
    printMajority(A)

    A = [1, 1, 1, 1, 1, 2, 3, 3]

    # Function call
    printMajority(A)
