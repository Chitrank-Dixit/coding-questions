# Python program to count all possible paths
# from top left to bottom right

# function to return count of possible paths
# to reach cell at row number m and column
# number n from the topmost leftmost
# cell (cell at 1, 1)
def numberOfPaths(m, n, memory={}):
    # If either given row number is first
    # or given column number is first
    if m == 1 or n == 1:
        return 1

    # If diagonal movements are allowed
    # then the last addition
    # is required.
    if f"{m},{n}" not in memory:
        memory[f"{m},{n}"] = numberOfPaths(m - 1, n) + numberOfPaths(m, n - 1)
    return memory[f"{m},{n}"]


if __name__ == "__main__":
    # Driver program to test above function
    m = 9
    n = 9
    print(numberOfPaths(m, n, {}))

    m = 18
    n = 18
    print(numberOfPaths(m, n, {}))
