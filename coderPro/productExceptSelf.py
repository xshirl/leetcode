class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        answer = [0] * length
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i-1] * answer[i-1]
        R = 1

        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer

    def product(self, nums):
        right = [1] * len(nums)
        product = 1

        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i+1]
            right[i] = product

        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            right[i] *= product

        return right

    def productExceptSelf2(self, nums):
        r = [1] * len(nums)
        print(r)

        anchor = 1
        # left
        for i in range(len(nums)):
            r[i] = anchor
            anchor *= nums[i]

        anchor = 1
        # right
        for i in range(len(nums)-1, -1, -1):
            r[i] *= anchor
            anchor *= nums[i]
        return r


print(Solution().product([1, 2, 3, 4]))
# [24, 12, 8, 6]
