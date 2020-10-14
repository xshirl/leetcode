import collections


class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = collections.defaultdict(int)
        begin = 0
        end = 0
        counter = 0
        K = 3
        ans = 0

        while end < len(s):
            ch = s[end]
            hashmap[ch] += 1
            if hashmap[ch] == 1:
                counter += 1

            while counter == K:
                # print s[begin : end + 1]
                ch = s[begin]
                hashmap[ch] -= 1
                if hashmap[ch] == 0:
                    counter -= 1
                begin += 1
                ans += len(s) - end
                # print s[begin : end + 1], ans

            end += 1

        return ans

# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/745969/Python-sliding-window-soln
