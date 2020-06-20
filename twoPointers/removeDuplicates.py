def removeDuplicates(nums):
    i, j = 0, 1

    while j < len(nums):
        if nums[i] != nums[j]:
            i += 1
            j += 1
        elif nums[i] == nums[j]:
            nums.pop(j)
    return len(nums)


print(removeDuplicates([1, 1, 2]))
