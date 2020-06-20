def strStr(haystack, needle):
    needleLen = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i+needleLen] == needle:
            return i
    if haystack == "" and needleLen > 0:
        return -1
    elif haystack == "":
        return 0
    return -1
