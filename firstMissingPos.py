def firstMissing(nums):
    res = 0
    for num in nums:
        if num == res:
            res += 1
    return res
