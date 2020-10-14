from collections import Counter


class Solution:
    def countCharacters(self, words, chars):
        sum = 0
        charCounter = Counter(chars)
        for word in words:
            wordCount = Counter(word)
            if all(wordCount[c] <= charCounter[c] for c in word):
                sum += len(word)
        return sum

# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
