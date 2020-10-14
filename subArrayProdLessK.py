class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if not nums:
            return 0
        count = 0
        prod = 1
        j = 0
        for i in range(len(nums)):
            prod *= nums[i]
            if prod >= k:
                while j <= i and prod >= k:
                    prod /= nums[j]
                    j += 1
            count += i - j + 1
        return count

# https://leetcode.com/problems/subarray-product-less-than-k/
