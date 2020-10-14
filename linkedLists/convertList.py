class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    # def __str__(self):
    #     c = self
    #     answer = ''
    #     while c:
    #         answer += str(c.val) if c.val else ""
    #         c = c.next
    #     return answer


def convert(arr):
    head = Node(arr[0])
    prev = head
    curr = None
    for i in range(1, len(arr)):
        curr = Node(arr[i])
        prev.next = curr
        prev = curr
        print(prev)
        curr = curr.next

    return head


answer = convert([1, 3, 5])
while answer:
    print(answer.val)
    answer = answer.next
