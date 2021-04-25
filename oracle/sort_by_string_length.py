def printArraystring(string, n):
    for i in range(n):
        print(string[i], end=" ")


# Function to Sort the array of string
# according to lengths. This function
# implements Insertion Sort.
def sort(s, n):
    for i in range(1, n):
        temp = s[i]

        # Insert s[j] at its correct position
        j = i - 1
        while j >= 0 and len(temp) < len(s[j]):
            s[j + 1] = s[j]
            j -= 1

        s[j + 1] = temp


# Driver code
if __name__ == "__main__":
    arr = ["GeeksforGeeks", "I", "from", "am"]
    n = len(arr)

    # Function to perform sorting
    sort(arr, n)

    # Calling the function to print result
    printArraystring(arr, n)
