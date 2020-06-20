def removeElement(nums, val):
    i = 0

    while i < len(nums):
        if nums[i] != val:
            i += 1
        else:
            nums.pop(i)

    return len(nums)

# https://leetcode.com/problems/remove-element/
