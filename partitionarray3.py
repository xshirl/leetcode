class Solution:
    def canThreePartsEqualSum(self, A):
        sumA = sum(A)
        if sumA % 3 != 0:
            return False
        req = sumA / 3
        sum2 = 0
        count = 0
        for i in range(len(A)):
            sum2 += A[i]
            if sum2 == req:
                sum2 = 0
                count += 1
        return count >= 3

# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/submissions/
