class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def arrayToList(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1, len(arr)):
        curr = Node(arr[i])
        prev.next = curr
        prev = curr
        curr = curr.next
    return head


print(arrayToList([1, 2, 3]))
