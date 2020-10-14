class Solution:
    def findKthPositive(self, arr, k):
        nums = []
        missing = []
        for i in range(1, max(arr) + k+1):
            nums.append(i)

        for num in nums:
            if num not in arr:
                missing.append(num)
        print(missing)
        return missing[k-1]
