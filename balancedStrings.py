class Solution:
    def balancedStringSplit(self, s: str) -> int:
        check = 0
        count = 0
        for x in s:
            if x == "R":
                check += 1
            if x == "L":
                check -= 1
            if check == 0:
                count += 1
        return count
