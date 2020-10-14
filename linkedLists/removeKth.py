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


class Solution:
    def remove_kth_from_list(self, node, k):
        slow, fast = node, node
        for i in range(k):
            fast = fast.next

        if not fast:
            return node.next

        prev = None
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
        prev.next = slow.next
        return node

    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
print(head)
# 12345

head = Solution().removeNthFromEnd(head, 2)
print(head)
# 1234

# 2,3,4,5
# 1,2,3,4

# 3,4,5
# 1,2,3,5
