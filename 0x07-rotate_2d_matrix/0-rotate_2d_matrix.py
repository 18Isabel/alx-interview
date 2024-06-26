#!/usr/bin/python3
"""rotate 2d matrix
"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp


# matrix = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
#
# rotate_2d_matrix(matrix)
# print(matrix)
