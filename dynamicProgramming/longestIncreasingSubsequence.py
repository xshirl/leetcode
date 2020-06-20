def longest(nums):
    if len(nums) == 0:
        return 0
    dp = [0 for x in range(len(nums))]
    dp[0] = 1
    maxAns = 1
    for i in range(1, len(dp)):
        maxVal = 0
        for j in range(i):
            if nums[i] > nums[j]:
                maxVal = max(maxVal, dp[j])
        dp[i] = maxVal + 1
        maxAns = max(maxAns, dp[i])

    return maxAns
