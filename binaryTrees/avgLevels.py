class Solution:
    def averageOfLevels(self, root):
        def dfs(root, level, res):
            if not root:
                return
            if len(res) < level+1:
                res.append([])
            res[level].append(root.val)
            dfs(root.left, level+1, res)
            dfs(root.right, level+1, res)
        res = []
        dfs(root, 0, res)
        avg = []
        for level in res:
            sumLevel = sum(level)
            avg.append(sumLevel/len(level))
        return avg
