def majorityElement(nums):
    dic = {}
    n = len(nums)

    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    for key, value in dic.items():
        if value > n/2:
            return key

# https://leetcode.com/problems/majority-element/
