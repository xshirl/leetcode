def restoreString(s, indices):
    arr = [k for k in s]
    res = [0] * len(indices)
    for j in range(len(s)):
        res[indices[j]] = arr[j]
    return "".join(res)


print(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
