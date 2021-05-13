"""
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the
matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word
'MASS', you should return true, since it's the last row.
"""


def find_word_in_matrix(matrix, word):
    i = 0
    j = 0
    while i < len(matrix):
        row_word = ""
        col_word = ""
        j = 0
        while j < len(matrix):
            row_word += matrix[i][j]
            col_word += matrix[j][i]
            j += 1
        if row_word == word or col_word == word:
            return True

        i += 1
    return False


if __name__ == "__main__":
    matrix = [
        ["F", "A", "C", "I"],
        ["O", "B", "Q", "P"],
        ["A", "N", "O", "B"],
        ["M", "A", "S", "S"],
    ]

    print(find_word_in_matrix(matrix, word="FOAM"))

    print(find_word_in_matrix(matrix, word="MASS"))

    print(find_word_in_matrix(matrix, word="ROAM"))
