class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for c in S:
            if c == "(":
                stack.append(0)
                print(stack)
            else:
                last = stack.pop()
                print(last)
                stack[-1] += 2*last or 1
                print(stack[-1])
                print(stack)
        return stack[0]


print(Solution().scoreOfParentheses("(())"))
