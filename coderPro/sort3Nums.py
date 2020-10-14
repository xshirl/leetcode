def sortNums(nums):
    one_index = 0
    three_index = len(nums) - 1
    index = 0
    while index <= three_index:
        if nums[index] == 1:
            nums[index], nums[one_index] = nums[one_index], nums[index]
            index += 1
            one_index += 1
        elif nums[index] == 2:
            index += 1
        elif nums[index] == 3:
            nums[index], nums[three_index] = nums[three_index], nums[index]
            three_index -= 1
    return nums


print(sortNums([3, 3, 2, 1, 2, 3, 1]))


def sortNums2(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    return [1] * counts[1] + [2] * counts[2] + [3] * counts[3]


print(sortNums2([3, 3, 2, 1, 2, 3, 1]))
