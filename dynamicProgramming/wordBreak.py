def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                print(dp[j])
                print(s[j:i])
                dp[i] = True
                break
    print(dp)
    return dp[-1]


print(wordBreak("applepenapple", ["apple", "pen"]))
