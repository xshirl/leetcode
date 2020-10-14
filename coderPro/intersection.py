class Solution:
    def intersection(self, nums1, nums2):
        result = {}
        for num in nums1:
            if num in nums2 and num not in result:
                result[num] = 1
        return list(result.keys())

    def intersection2(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return [x for x in set1 if x in set2]

    def intersection3(self, nums1, nums2):
        res = {}
        dup = {}
        for i in nums1:
            res[i] = 1
        for i in nums2:
            if i in res:
                dup[i] = 1
        return list(dup.keys())


print(Solution().intersection3([4, 9, 5], [9, 4, 9, 8, 4]))
