class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        arr = [i for i in word]
        if word.isupper():
            return True
        if word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return False


print(Solution().detectCapitalUse('USA'))
print(Solution().detectCapitalUse('FlaG'))
