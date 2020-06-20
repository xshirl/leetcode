def numDecoding(s):
    if not s or s.startswith('0'):
        return 0

    stack = [1, 1]

    for i in range(1, len(s)):
        if s[i] == '0':
            if s[i-1] == '0' or s[i-1] > '2':
                return 0
            stack.append(stack[-2])
        elif 9 < int(s[i-1:i+1]) < 27:
            stack.append(stack[-2] + stack[-1])
        else:
            stack.append(stack[-1])
    return stack[-1]


def numDecodings2(s):
    def helper(i):
        if i in dic:
            return dic[i]
        if i >= len(s):
            return 1
        res = 0
        if 1 <= int(s[i]) <= 9:
            res += helper(i+1)
        if 10 <= int(s[i:i+2]) <= 26:
            res += helper(i+2)
        dic[i] = res
        return res
    dic = {}
    return helper(0) if s else 0

# https://leetcode.com/problems/decode-ways/discuss/240637/Python-solution
