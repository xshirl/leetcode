class Solution:
    def levelOrder(self, root):

        def bfs(root, level, res):
            if not root:
                return
            if len(res) < level+1:
                res.append([])
            res[level].append(root.val)
            bfs(root.left, level+1, res)
            bfs(root.right, level+1, res)
        res = []
        bfs(root, 0, res)
        return res
