def findAnagrams(s, p):
    dic = {}
    res = []
    for char in p:
        dic[char] = dic.get(char, 0) + 1
    i = 0
    j = len(p)
    while j < len(s) + 1:
        dic2 = {}
        for char in s[i:j]:
            if char in dic:
                dic2[char] = dic2.get(char, 0) + 1
            if dic2 == dic:
                res.append(i)
        i += 1
        j += 1

    return res


print(findAnagrams("abab", "ab"))


def checkInclusion(s1, s2):
    dic = {}
    for char in s1:
        dic[char] = dic.get(char, 0) + 1
    print(dic)
    for i in range(len(s2) - len(s1) + 1):
        dic2 = {}
        for char in s2[i:i+len(s1)]:
            if char in dic:
                dic2[char] = dic2.get(char, 0) + 1
            print(dic2)
            if dic2 == dic:
                return True
    return False


print(checkInclusion("ab", "dab"))
