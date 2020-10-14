from collections import defaultdict


class Solution:
    def sortColors(self, colors):
        colorsMap = defaultdict(int)
        for c in colors:
            colorsMap[c] += 1

        index = 0
        print(colorsMap)
        for i in range(colorsMap[0]):
            colors[index] = 0
            index += 1

        for i in range(colorsMap[1]):
            colors[index] = 1
            index += 1

        for i in range(colorsMap[2]):
            colors[index] = 2
            index += 1

    def sortColors2(self, colors):
        low = 0
        high = len(colors) - 1
        curr = 0

        while curr <= high:
            if colors[curr] == 0:
                colors[low], colors[curr] = colors[curr], colors[low]
                low += 1
                curr += 1
            elif colors[curr] == 2:
                colors[high], colors[curr] = colors[curr], colors[high]
                high -= 1
            else:
                curr += 1


colors = [0, 2, 1, 0, 1, 1, 2]
Solution().sortColors2(colors)
print(colors)
