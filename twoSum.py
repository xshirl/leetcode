def twoNumberSum(array, targetSum):
    # Write your code here.
    hashTable = {}
    res = []
    for num in array:
        hashTable[num] = targetSum - num
    for num in array:
        if num in hashTable and hashTable[num] in array and num not in res and hashTable[num] not in res:
            res.append(num)
            array.remove(num)
            if hashTable[num] in array:
                res.append(hashTable[num])
            else:
                res.remove(num)

    return res


print(twoNumberSum([1, 3, 4, 5], 8))
