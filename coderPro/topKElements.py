import collections


class Solution:
    def topKElements(self, nums, k):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        res = []
        maxCount = 0
        for key in sorted(dic, key=dic.get, reverse=True):
            res.append(key)
        return res[:k]

    def topKFrequent(self, words, k):
        C = collections.Counter(words)
        S = sorted(C.keys(), key=lambda x: [-C[x], x])
        return S[:k]


print(Solution().topKElements([1, 1, 1, 2, 2, 2, 2, 3], 2))
