def robber(nums):
    if len(nums) == 0:
        return 0

    b = nums[::1]

    for i in range(2, len(nums) - 1):
        if i == 2:
            nums[i] += nums[i-2]
        else:
            nums[i] += max(nums[i-2], nums[i-3])

    for i in range(3, len(b)):
        if i == 3:
            b[i] += b[i-2]
        else:
            b[i] += max(b[i-2], b[i-3])

    return max(max(nums), max(b))
