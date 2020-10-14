class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return self.val


class Solution:
    def depth(self, root):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        max_depth = max(left_depth, right_depth) + 1
        return max_depth

    def deepest(self, node):
        if not node:
            return 0
        return 1 + max(self.deepest(node.left), self.deepest(node.right))


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.left.left.right = Node('e')
root.right = Node('c')

print(Solution().deepest(root))
# 4
