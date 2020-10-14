from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        c1 = Counter(s)
        c2 = Counter()
        res = 0
        for char in s:
            c2[char] += 1
            c1[char] -= 1
            if c1[char] == 0:
                del c1[char]
            if len(c2) == len(c1):
                res += 1
        return res

        # https://leetcode.com/problems/number-of-good-ways-to-split-a-string/submissions/
