class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def symmetric(root: TreeNode) -> bool:
    def check(p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val != q.val:
            return False
        return check(p.left, q.right) and check(p.right, q.left)
    check(root, root)
