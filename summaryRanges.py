def summaryRanges(nums):
    result = []
    continous = False
    start = 0
    for i in range(len(nums)):
        if i+1 < len(nums) and continous == False and nums[i+1] == nums[i] + 1:
            continous = True
            start = nums[i]
        elif continous == True:
            if i+1 == len(nums) or nums[i+1] != nums[i] + 1:
                result_string = str(start) + "->" + str(nums[i])
                result.append(result_string)
                continous = False
        else:
            result.append(str(nums[i]))
    return result

# https://leetcode.com/problems/summary-ranges/submissions/
