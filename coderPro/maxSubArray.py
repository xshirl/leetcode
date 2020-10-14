def maxSubArray(nums):
    maxSum = 0
    sum = 0
    for n in nums:
        sum += n
        if sum < 0:
            sum = 0
        else:
            maxSum = max(maxSum, sum)
    return maxSum


print(maxSubArray([-1, -4, 3, 8, 1]))
