def twoSum(nums, target):
    i = 0
    j = len(nums) - 1
    sortedNums = sorted(zip(nums, range(len(nums))))
    print(sortedNums)
    while i < j:
        if sortedNums[i][0] + sortedNums[j][0] == target:
            return [sortedNums[i][1], sortedNums[j][1]]
        elif sortedNums[i][0] + sortedNums[j][0] < target:
            i += 1
        elif sortedNums[i][0] + sortedNums[j][0] > target:
            j -= 1


print(twoSum([1, 2, 5, 3], 7))

# two pointer method
