def maxSubArray(nums):
    maxCurrent = maxGlobal = nums[0]
    for i in range(1, len(nums)):
        maxCurrent = max(maxCurrent + nums[i], nums[i])
        if maxGlobal < maxCurrent:
            maxGlobal = maxCurrent
    return maxGlobal
