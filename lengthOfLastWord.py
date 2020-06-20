def lengthLastWord(s):
    s = s.strip()
    arr = s.split(" ")
    if len(arr) > 0:
        return len(arr[-1])
    return 0
