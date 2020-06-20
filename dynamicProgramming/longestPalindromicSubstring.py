def longestPalindrome(s):
    maxString = ""

    def twoPointer(i, j, s):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]

    for i in range(len(s)):
        string1 = twoPointer(i, i, s)
        if len(string1) > len(maxString) or not maxString:
            maxString = string1
        string2 = twoPointer(i, i+1, s)
        if len(string2) > len(maxString) or not maxString:
            maxString = string2

    return maxString
