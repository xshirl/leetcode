class Solution:
    def reconstructQueue(self, input):
        input.sort(key=lambda x:
                   (-x[0], x[1])
                   )
        res = []
        for person in input:
            res.insert(person[1], person)
        return res


input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().reconstructQueue(input))

# We first sort the list people, in the order of descending height. If multiple people are of the same height, sort them in ascending order of the number of people in front of them. For example, if people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]], after the line people_sorted = sorted(people, key = lambda x: (-x[0],x[1])), people_sorted = [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]. Then for each person [i,j], their index in people_sorted is larger than or equal to j (due to the way we sort people). Hence to obtain the final results, we just need to construct an empty list res, and starting from the left, insert each element [i,j] in people_sorted to position j in res (Latter insertions of [i',j'] won't affect j because either i' < i, or i' == i and j' > j). The time complexity of the algorithm is O(n^2): We loop over people once, and each insertion is an O(n) operation. The space complexity is O(n).

# We illustrate the above procedure with people_sorted, as i goes from 0 to 5, the empty list res changes as follows:
