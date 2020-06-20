def removeDuplicates(nums):
    i, j = 0, 1

    while j < len(nums):
        if nums[i] != nums[j]:
            i += 1
            j += 1
        else:
            nums.pop(j)

    return len(nums)

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
