
class Node(object):

    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data

    def is_leaf(self):
        return self.left is None and self.right is None
