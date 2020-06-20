def minSubArrayLen(self, s, nums):
    i, res = 0, len(nums) + 1
    for j in range(len(nums)):
        s -= nums[j]
        while s <= 0:
            res = min(res, j - i + 1)
            s += nums[i]
            i += 1
    return res % (len(nums) + 1)

# https://leetcode.com/problems/minimum-size-subarray-sum/discuss/433123/JavaC%2B%2BPython-Sliding-Window


def minSubArrayLen2(s, nums):
    total = left = right = 0
    res = len(nums) + 1

    while right < len(nums):
        total += nums[right]
        while total >= s:
            res = min(res, right - left + 1)
            total -= nums[left]
            left += 1
        right += 1
    return res if res <= len(nums) else 0

# O(n) time
# we scan from left to right, "total" tracks the
# sum of the subarray. If the sum is less than s,
# right moves forward one step, else left moves forward
# one step, left and right form a window.
