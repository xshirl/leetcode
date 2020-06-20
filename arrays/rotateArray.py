def rotate(nums, k):
    n = len(nums)

    for _ in range(k):
        last = nums[-1]
        nums[1:n] = nums[0:n-1]
        nums[0] = last


# https://leetcode.com/problems/rotate-array/
