import collections


class Solution:
    def findOcurrences(self, text, first, second):
        res = []
        text = text.split()
        dic = collections.defaultdict(list)
        for i in range(len(text)):
            dic[text[i]].append(i)
        for key, idx in dic.items():
            if first == key:
                for i in idx:
                    if len(text) - 1 >= i + 2 and second == text[i+1]:
                        res.append(text[i+2])
        return res

        # https://leetcode.com/problems/occurrences-after-bigram/submissions/
