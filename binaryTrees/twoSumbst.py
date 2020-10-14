class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# sort through values in an inorder way, maked a sorted array, then use two pointer
# method to find two sum.


def twoSum(root: TreeNode, k: int) -> bool:
    if not root:
        return False

    def inorder(root):
        if not root:
            return
        if root:
            if not root.left and not root.right:
                return [root.val]
        left = inorder(root.left) or []
        right = inorder(root.right) or []
        return left + [root.val] + right
    res = inorder(root)
    i = 0
    j = len(res)-1
    while i < j:
        sum = res[i] + res[j]
        if sum == k:
            return True
        elif sum < k:
            i += 1
        else:
            j -= 1
    return False
