def removeDuplicates(nums):
    dic = {}

    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    for num, count in dic.items():
        while count > 2:
            nums.remove(num)
            count -= 1

    return len(nums)

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
