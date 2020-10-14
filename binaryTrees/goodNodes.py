class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0

        def dfs(node, m):
            if node:
                if node.val >= m:
                    self.res += 1
                    m = node.val
                dfs(node.left, m)
                dfs(node.right, m)
        dfs(root, -float("inf"))
        return self.res

# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
