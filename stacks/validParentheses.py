class Solution:
    def isValid(self, s):
        stack = []
        openParen = ["(", "[", "{"]
        closedParen = [")", "]", "}"]

        if s == "":
            return True

        for paren in s:
            if paren in openParen:
                stack.append(paren)
            elif paren in closedParen:
                i = closedParen.index(paren)
                if (len(stack) > 0) and stack[len(stack)-1] == openParen[i]:
                    stack.pop()
        return len(stack) == 0


print(Solution().isValid('(){([])}'))
print(Solution().isValid('(){(['))
