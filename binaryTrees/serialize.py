class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result


def serialize(node):
    if node == None:
        return '#'
    return str(node.val) + ' ' + serialize(node.left) + ' ' + serialize(node.right)


def deserialize(str):
    def deserialize_helper(values):
        value = next(values)
        if value == '#':
            return None
        node = Node(int(value))
        node.left = deserialize_helper(values)
        node.right = deserialize_helper(values)
        return node
    values = iter(str.split())
    return deserialize_helper(values)
