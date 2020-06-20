def findMedian(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    length = len(nums1)
    if length == 1:
        return float(nums1[0])
    elif length % 2 != 0:
        return (float(nums1[int((length+1)/2)-1]))
    else:
        div1 = nums1[int((length/2)-1)]
        div2 = nums1[int(((length+2)/2) -1)]
        return (div1 + div2)/2


