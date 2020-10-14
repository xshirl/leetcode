def luckyNumbers(matrix):
    res = []
    colNums = []
    rowNums = []

    def col(matrix, i):
        rowNums = [row[i] for row in matrix]
        return rowNums
    maxNums = []
    minNums = []
    i = 0
    while i < len(matrix[0]):
        maxNums.append(max(col(matrix, i)))
        i += 1
    for i in range(len(matrix)):
        minNums.append(min(matrix[i]))
    for num in maxNums:
        if num in minNums:
            res.append(num)
    print(minNums)
    print(maxNums)
    return res


print(luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
