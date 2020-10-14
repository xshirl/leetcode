class Solution:
    def __evalHelper(self, expression, index):
        op = "+"
        result = 0
        while index < len(expression):
            char = expression[index]
            if char in ("+", "-"):
                op = char
            else:
                value = 0
                if char.isdigit():
                    value = int(char)
                elif char == '(':
                    (value, index) = self.__evalHelper(expression, index+1)
                if op == '+':
                    result += value
                if op == "-":
                    result -= value
            index += 1
        return (result, index)

    def eval(self, expression):
        return self.__evalHelper(expression, 0)


print(Solution().eval('(1 + (2 + (3 + (4 + 5))))'))
# 15
