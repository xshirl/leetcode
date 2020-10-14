class Solution:
    def checkPossibility(self, nums):
        invalid = -1

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if invalid != -1:
                    return False
                invalid = i

        if invalid == 0 or invalid == len(nums) - 2 or invalid == -1:
            return True
        if nums[invalid] <= nums[invalid+2]:
            return True
        if nums[invalid - 1] <= nums[invalid + 1]:
            return True
        return False


print(Solution().checkPossibility([4, 1, 2]))
# True

print(Solution().checkPossibility([3, 2, 4, 1]))
# False
