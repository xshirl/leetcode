def search(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return True
        while l < mid and nums[l] == nums[mid]:  # tricky part
            l += 1
        # the first half is ordered
        if nums[l] <= nums[mid]:
            # target is in the first half
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # the second half is ordered
        else:
            # target is in the second half
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return False


def search2(nums, target):
    left, right = 0, len(nums) - 1
    # to distinguish left ascending array and right ascending array
    while left < right and nums[left] == nums[right]:
        left += 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        if nums[left] <= nums[mid]:                         # nums[mid] at left ascending array
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            # nums[mid] < target
            else:
                left = mid + 1
        # nums[mid] at right ascending array
        elif nums[mid] <= nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            # nums[mid] > target
            else:
                right = mid - 1
    return False
