class Solution:
    def lastStoneWeight(self, x):
        l = len(x)
        if l == 0:
            return 0
        if len(x) == 1:
            return x[0]
        while True:
            if len(x) == 1:
                return x[0]
            if len(x) == 0:
                return 0
            x = sorted(x, reverse=True)
            a = x[0]
            b = x[1]
            if a == b:
                x = x[2:]
            else:
                x[1] = a-b
                del x[0]
