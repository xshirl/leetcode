def countOdds(low, high):
    res = []
    for i in range(low, high+1):
        if i & 1:
            res.append(i)
    return res


print(countOdds(3, 7))


def numOfSubarrays(arr):
    count = 0
    for i in range(0, len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum = sum + arr[j]
            if sum & 1:
                count += 1
    return count
    # res = [[]]
    # for n in arr:
    #     for i in range(len(res)):
    #         res.append(res[i]+[n])
    # count = 0
    # print(res)
    # for i in range(len(res)):
    #     if sum(res[i]) & 1:
    #         count += 1
    # return count


print(numOfSubarrays([1, 3, 5]))

# [[1],[1,3],[1,3,5],[3],[3,5],[5]]
