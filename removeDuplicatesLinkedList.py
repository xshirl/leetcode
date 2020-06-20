def deleteDuplicates(head):
    curr, prev = head, head

    if curr == None or curr.next == None:
        return head

    while curr:
        if curr.val == prev.val:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
    return head
