class Solution:
    def minNumberOperations(self, target): d
        res = pre = 0
        for a in target:
            res += max(a-pre, 0)
            pre = a
        return res

        # https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
