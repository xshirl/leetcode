# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root):
        return self.findDepth(root) != -1

    def findDepth(self, root):
        if not root:
            return 0
        lDepth = self.findDepth(root.left)
        rDepth = self.findDepth(root.right)
        if lDepth == -1 or rDepth == -1 or abs(lDepth-rDepth) > 1:
            return -1
        return max(lDepth, rDepth) + 1

# https://leetcode.com/problems/balanced-binary-tree/discuss/721515/Python-DFS
