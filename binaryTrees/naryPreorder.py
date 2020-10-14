class Solution:
    def preorder(self, root):
        res = []

        def dfs(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                dfs(child)
        dfs(root)
        return res
