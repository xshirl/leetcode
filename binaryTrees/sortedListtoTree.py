# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        def convert(node, res):
            while node:
                res.append(node.val)
                node = node.next

        def dfs(arr, low, high):
            if low <= high:
                mid = low + (high-low) // 2
                node = TreeNode(arr[mid])
                node.left = dfs(arr, low, mid-1)
                node.right = dfs(arr, mid+1, high)
                return node
            return None
        res = []
        convert(head, res)
        root = dfs(res, 0, len(res) - 1)
        return root
