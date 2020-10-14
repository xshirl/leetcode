class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        res = []
        if not root:
            return res
        self.dfs(root, "", res)
        return res

    def dfs(self, root, path, paths):
        path += str(root.val)
        if not root.left and not root.right:
            paths.append(path)
        if root.left:
            self.dfs(root.left, path + "->", paths)
        if root.right:
            self.dfs(root.right, path + "->", paths)
