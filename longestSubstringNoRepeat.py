class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        letter_pos = {}
        start = -1
        end = 0
        max_length = 0

        while end < len(str):
            c = str[end]
            if c in letter_pos:
                start = max(start, letter_pos[c])

            max_length = max(max_length, end - start)

            letter_pos[c] = end
            end += 1
        return max_length

# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/


def longest(str):
    letter_pos = {}
    start = -1
    end = 0
    max_length = 0

    while end < len(str):
        c = str[end]
        if c in letter_pos:
            start = max(start, letter_pos[c])
            print(start)
        max_length = max(max_length, end - start)
        print(max_length)
        letter_pos[c] = end
        end += 1
    return max_length

# abcbefgha


# print(longest("abcbefgha"))


def lengthOfLongestSubstring(s):
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in dic:
            # update the res
            res = max(res, i-start)
            # here should be careful, like "abba"
            start = max(start, dic[ch]+1)
        dic[ch] = i
    # return should consider the last
    # non-repeated substring
    return max(res, len(s)-start)


print(lengthOfLongestSubstring("abcbefgha"))
