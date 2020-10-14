def largeGroupPositions(self, S):
    res = []
    prev = S[0]
    prev_idx = 0
    for i in range(len(S)):
        if S[i] != prev:
            if i - prev_idx >= 3:
                res.append([prev_idx, i-1])
            prev_idx = i
            prev = S[i]
    if len(S) - prev_idx >= 3:
        res.append([prev_idx, len(S)-1])
    return res

# https://leetcode.com/problems/positions-of-large-groups/
