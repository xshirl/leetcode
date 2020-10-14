class Solution:
    def kClosest(self, points, K):
        points.sort(key=lambda x: x[0] * x[0] + x[1] * x[1])
        return points[:K]

# https://leetcode.com/problems/k-closest-points-to-origin/
