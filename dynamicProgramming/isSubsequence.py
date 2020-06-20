def isSubsequence(s, t):
    arrT = t.split("")
    dp = [False] * len(s)
    for j in range(len(s)):
        if s[j] in arrT:
            dp[j] = True

    return all(dp)


def isSubsequence2(self, s: str, t: str) -> bool:
    if len(t) < len(s):
        return False
    indx = 0
    for val in s:
        if indx > len(t)-1:
            return False
        if val in t[indx:]:
            indx = t.index(val, indx) + 1
        else:
            return False
    return True


def subsequence(s, t):
    m, n = len(s), len(t)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if not i or not j:
                dp[i][j] = 0
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[-1][-1] == m
