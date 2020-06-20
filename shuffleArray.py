def shuffle(nums, n):
    i = 0
    j = n
    res = []
    while i < j:
        res.append(nums[i])
        res.append(nums[n])
        i += 1
        n += 1
    return res

# https://leetcode.com/problems/shuffle-the-array/submissions/
