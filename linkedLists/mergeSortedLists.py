class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def mergeSorted(l1, l2):
    curr = Node(0)
    head = curr

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        elif l1.val >= l2.val:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    if not l1:
        curr.next = l2
    if not l2:
        curr.next = l1

    return head.next

# https://leetcode.com/problems/merge-two-sorted-lists/
