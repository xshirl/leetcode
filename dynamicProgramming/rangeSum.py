class NumArray:

    def __init__(self, nums):
        self.dp = [0 for i in range(len(nums) + 1)]
        sum = 0
        for i in range(1, len(nums)+1):
            sum += nums[i-1]
            self.dp[i] = sum

    def sumRange(self, i, j):
        return self.dp[j+1] - self.dp[i]
