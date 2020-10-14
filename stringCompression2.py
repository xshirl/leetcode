from collections import Counter


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        c = Counter(s)
        string = ""
        for key, value in c.items():
            # if value - k <= 0 and k > 0:
            #     k -= value
            # elif value - k > 0:
            string += key + str(value)

        return string


print(Solution().getLengthOfOptimalCompression("aabbaa", 2))
