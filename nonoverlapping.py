def eraseOverlapIntervals(self, intervals):
    if intervals == []:
        return 0
    intervals = sorted(intervals, key=lambda intervals: intervals[1])
    ans = 0
    left, right = intervals[0]
    for i in range(1, len(intervals)):
        if right <= intervals[i][0]:
            left, right = intervals[i]
        else:
            ans += 1
    return ans


# https: // leetcode.com/problems/non-overlapping-intervals/submissions/
