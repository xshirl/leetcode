def maxArea(height):
    l = 0
    r = len(height) - 1
    area = (r-l) * min(height[l], height[r])
    while l < r:
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        area = max(area, (r-l)*min(height[l], height[r]))
    return area

# https://leetcode.com/problems/container-with-most-water/
