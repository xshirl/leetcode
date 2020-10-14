class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def _length(self, n):
        curr = n
        length = 0
        while curr:
            curr = curr.next
            length += 1

        return length

    def intersection(self, a, b):
        currA = a
        currB = b

        lenA = self._length(a)
        lenB = self._length(b)

        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next

        while currA != currB:
            currA = currA.next
            currB = currB.next

        return currA


a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

print(Solution().intersection(a, b).val)
