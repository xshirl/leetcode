class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    currentNode = ListNode(0)
    head = currentNode

    while l1 and l2:
        if l1.val < l2.val:
            currentNode.next = l1
            l1 = l1.next
        elif l1.val >= l2.val:
            currentNode.next = l2
            l2 = l2.next
        currentNode = currentNode.next

    if not l1:
        currentNode.next = l2

    if not l2:
        currentNode.next = l1

    return head.next

    # https://leetcode.com/problems/merge-two-sorted-lists/
