import collections


def subarraySum(nums, k):
    counter = collections.Counter()
    counter[0] = 1
    answer = numSum = 0
    for x in nums:
        numSum += x
        answer += counter[numSum - k]
        counter[numSum] += 1
    return answer

# https://leetcode.com/problems/subarray-sum-equals-k