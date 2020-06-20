def longestSubstring(s):
    length = []
    maxLength = 0

    for i in range(len(s)):
        if s[i] not in length:
            length.append(s[i])
        else:
            idx = length.index(s[i])
            length.append(s[i])
            length = length[idx+1:]
        if len(length) > maxLength:
            maxLength = len(length)

    return maxLength

# https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
