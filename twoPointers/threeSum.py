def threeSum(nums):
    nums.sort()
    res = []
    if len(nums) < 3:
        return res

    for i in range(len(nums)-2):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res

# https://leetcode.com/problems/3sum/
