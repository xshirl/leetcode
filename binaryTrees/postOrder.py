class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode):
        if not root:
            return []
        if root:
            if not root.left and not root.right:
                return [root.val]
        left = self.postorderTraversal(root.left) or []
        right = self.postorderTraversal(root.right) or []
        return left + right + [root.val]
