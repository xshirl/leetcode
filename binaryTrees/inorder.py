class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        if root:
            if not root.left and not root.right:
                return [root.val]
        left = self.inorderTraversal(root.left) or []
        right = self.inorderTraversal(root.right) or []
        return left + [root.val] + right
