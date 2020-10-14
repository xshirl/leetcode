class Solution:
    def summaryRanges(self, nums):

        def makeRange(low, high):
            if low != high:
                return str(low) + "->" + str(high)
            return str(low)

        if not nums:
            return []
        ranges = []

        low = high = nums[0]

        for n in nums:
            if high + 1 < n:
                ranges.append(makeRange(low, high))
                low = n
            high = n

        ranges.append(makeRange(low, high))

        return ranges
