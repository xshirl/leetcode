class Solution:
    def maxScore(self, s: str) -> int:
        maxScore = 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            leftCount = 0
            rightCount = 0
            for i in left:
                if i == "0":
                    leftCount += 1
            for i in right:
                if i == "1":
                    rightCount += 1
            print("leftCount", i, leftCount)
            print("rightCount", i, rightCount)
            if leftCount + rightCount > maxScore:
                maxScore = leftCount + rightCount
                print("maxScore", i, maxScore)
        return maxScore


print(Solution().maxScore("1111"))
