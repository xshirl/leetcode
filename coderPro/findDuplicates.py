class Solution():
    def findDuplicates(self, nums):
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for key, value in hashmap.items():
            if value == 1:
                return key

    def singleNumber(self, nums):
        unique = 0
        for n in nums:
            unique ^= n
        return unique


print(Solution().findDuplicates([4, 4, 3, 3, 2, 2, 1])

      )

# A number XOR itself will get result 0. And a number XOR 0 will get itself. For example,

# >>> 1 ^ 1
# 0
# >>> 0 ^ 2
# 2
