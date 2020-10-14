# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(root, parent, depth, node):
            res = []
            if root:
                if root.val == node:
                    res.append(depth)
                    res.append(parent)
                    return res
                return dfs(root.left, root, depth+1, node) or dfs(root.right, root, depth+1, node)
        dx = dfs(root, None, 0, x)[0]
        dy = dfs(root, None, 0, y)[0]
        px = dfs(root, None, 0, x)[1]
        py = dfs(root, None, 0, y)[1]

        return dx == dy and px != py
