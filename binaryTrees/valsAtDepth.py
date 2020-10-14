class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def valuesAtLevel(self, node, depth):
        if not node:
            return []
        if depth == 1:
            return [node.val]
        return self.valuesAtLevel(node.left, depth-1) + self.valuesAtLevel(node.right, depth - 1)


node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.right.right = Node(7)
node.left.left = Node(4)
node.left.right = Node(5)

print(Solution().valuesAtLevel(node, 3))

# get all values at certain height on tree
