def searchRange(nums, target):
    if target not in nums:
        return [-1, -1]
    res = []
    res.append(nums.index(target))
    res.append(len(nums) - 1 - nums[::-1].index(target))
    return res

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/
