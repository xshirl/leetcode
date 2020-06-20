def pascal(numRows):
    res = [[1], [1, 1]]
    if numRows == 0:
        return []
    elif numRows == 1:
        return [res[0]]

    for i in range(2, numRows):
        counter = 1
        temp = [1, 1]
        for j in range(len(res[i-1])-1):
            temp.insert(counter, res[i-1][j] + res[i-1][j+1])
            counter += 1
        res.append(temp)

    return res
