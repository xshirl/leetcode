def removeDuplicates(nums):
    pointer = 0

    while pointer < len(nums):
        cur = nums[pointer]
        count = 0
        while pointer < len(nums) and nums[pointer] == cur:
            pointer += 1
            count += 1
        if count > 2:
            nums[:] = nums[:pointer-count+2] + nums[pointer:]
            pointer = pointer - count + 2
    return len(nums)


def removeDuplicates2(nums):
    slow = fast = 0
    while fast < len(nums):
        while fast < len(nums) and nums[slow] == nums[fast]:
            fast += 1
        if fast-slow > 2:
            for _ in range(fast-slow+2):
                nums.pop(slow)
            slow = fast = fast - (fast - slow - 2)
        else:
            slow = fast

    return len(nums)

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
