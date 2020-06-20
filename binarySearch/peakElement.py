def findPeakElement(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[mid+1]:
            low = mid + 1
        else:
            high = mid

    return low

# https://leetcode.com/problems/find-peak-element/
