def kWeakestRows(mat, k):
    res = []
    for i in range(len(mat)):
        soldiers = [0, 0]
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                soldiers[0] += 1
            soldiers[1] = i
        res.append(soldiers)
    res.sort(key=lambda x: x[0])
    weakest = []
    for arr in res[:k]:
        weakest.append(arr[1])
    return weakest
