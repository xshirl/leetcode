def validParen(s):
    stack = []
    opened = ["(", "{", "["]
    closed = [")", "}", "]"]

    if s == "":
        return True

    for paren in s:
        if paren in opened:
            stack.append(paren)
        if paren in closed:
            idx = closed.index(paren)
            if (len(stack) > 0 and (stack[len(stack)-1] == opened[idx])):
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True


print(validParen("{})"))

# https://leetcode.com/problems/valid-parentheses/
