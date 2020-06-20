import itertools


def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    row, col = set(), set()
    for i, j in itertools.product(range(m), range(n)):
        if not matrix[i][j]:
            row.add(i)
            col.add(j)

    for i, j in itertools.product(range(m), range(n)):
        if i in row or j in col:
            matrix[i][j] = 0


def setZeroes2(matrix):
    m, n = len(matrix), len(matrix[0])
    zero = False

    for i in range(m):
        if not matrix[i][0]:
            zero = True
        for j in range(1, n):
            if not matrix[i][j]:
                matrix[i][0] = matrix[0][j] = 0

    for i in reversed(range(m)):
        for j in reversed(range(1, n)):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0
        if zero:
            matrix[i][0] = 0

# https://leetcode.com/problems/set-matrix-zeroes/submissions/
