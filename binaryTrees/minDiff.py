# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = []

        def inorder(root):
            if root.left:
                inorder(root.left)
            res.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        res2 = zip(res, res[1:])
        print(res2)
        return min(b-a for a, b in zip(res, res[1:]))


res = [1, 3, 2]
print(set(zip(res, res[1:])))
