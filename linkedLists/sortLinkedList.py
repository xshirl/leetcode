class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def sortedMerge(self, a, b):
        result = None
        if a is None:
            return b
        if b is None:
            return a
        if a.val <= b.val:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        
        middle = self.getMiddle(head)
        middleNext = middle.next
        middle.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(middleNext)
        sortedList = self.sortedMerge(left, right)
        return sortedList

    def getMiddle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next 
        return slow 

