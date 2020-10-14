class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):
        n = self
        answer = ""
        while n:
            answer += str(n.val)
            n = n.next
        return answer


class Solution():
    def sumList(self, head):
        numSum = 0
        while head:
            numSum += head.val
            head = head.next
        return numSum


head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
print(head)
# 12345

head = Solution().sumList(head)
print(head)
