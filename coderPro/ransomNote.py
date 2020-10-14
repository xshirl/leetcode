from collections import defaultdict


class Solution(object):
    def canSpell(self, magazine, note):
        letters = {}
        for char in magazine:
            letters[char] = letters.get(char, 0) + 1
        print(letters)
        for char in note:
            if letters[char] <= 0:
                return False
            letters[char] -= 1

        return True

    def canSpell2(self, magazine, note):
        letters = defaultdict(int)
        for char in magazine:
            letters[char] += 1
        print(letters)
        for char in note:
            if letters[char] <= 0:
                return False
            letters[char] -= 1
        print(letters)
        return True


print(Solution().canSpell2(['a', 'b', 'b', 'c', 'd', 'e'], "bed"))
