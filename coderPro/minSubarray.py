class Solution:
    def minSubarray(self, k, nums):
        left_index = right_index = 0
        minLen = float("inf")
        sum = 0

        while right_index < len(nums):
            sum += nums[right_index]
            while sum >= k:
                minLen = min(minLen, right_index - left_index+1)
                sum -= nums[left_index]
                left_index += 1
            right_index += 1

        if minLen == float('inf'):
            return 0
        return minLen


print(Solution().minSubarray(7, [2, 3, 1, 2, 4, 3]))
