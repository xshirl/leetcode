import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        output = []
        nums = []
        for num in range(1, n+1):
            nums.append(num)
        m = len(nums)

        def permute(first=0):
            if first == m:
                output.append(nums[:])
            for i in range(first, m):
                nums[first], nums[i] = nums[i], nums[first]
                permute(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        permute()
        new_output = []
        for i in range(len(output)):
            string = "".join(map(str, output[i]))
            new_output.append(string)
        maxNum = 0
        for i in range(len(new_output)):
            new_output[i] = int(new_output[i])
        new_output.sort()
        return str(new_output[k-1])


def getPermutation(n, k):
    k -= 1
    l = list(range(1, n+1))
    o = ''
    for p in range(n):
        f = int(math.factorial(n-p-1))
        x, k = k//f, k % f
        o += str(l[x])
        l.remove(l[x])
    return o
