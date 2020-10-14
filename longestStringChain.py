class Solution:
    def longestStrChain(self, words):
        words.sort(key=lambda x: len(x))
        answer = 1
        chain = {}

        for word in words:
            for i in range(len(word)):
                sub = word[:i] + word[i+1:]
                print(word, sub, i)
                if sub in chain:
                    chain[word] = chain[sub] + 1
                    answer = max(answer, chain[word])
            if word not in chain:
                chain[word] = 1
        return answer

# https://leetcode.com/problems/longest-string-chain/discuss/633379/Python


print(Solution().longestStrChain(
    ["a", "b", "ba", "bca", "bda", "bdca"]))
