class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode):
        if not root:
            return []
        if root:
            if not root.right and not root.left:
                return [root.val]
        left = self.preorderTraversal(root.left) or []
        right = self.preorderTraversal(root.right) or []
        return [root.val] + left + right
