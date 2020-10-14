import collections


class Solution:
    def levelOrder(self, root):
        tree = collections.defaultdict(list)
        self.helper(root, tree, 0)
        return [v for v in tree.values()]

    def helper(self, root, tree, level):
        if not root:
            return
        tree[level].append(root.val)
        for child in root.children:
            self.helper(child, tree, level+1)
