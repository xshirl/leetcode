class Solution:
    def _permuteHelper(self, nums, start=0):
        if start == len(nums) - 1:
            return [nums[:]]

        result = []

        for i in range(start, len(nums)):
            nums[i], nums[start] = nums[start], nums[i]
            print(nums)
            result += self._permuteHelper(nums, start + 1)
            nums[i], nums[start] = nums[start], nums[i]
            print(nums)

        return result

    def permutations(self, nums):
        return self._permuteHelper(nums)


print(Solution().permutations([1, 2, 3]))
