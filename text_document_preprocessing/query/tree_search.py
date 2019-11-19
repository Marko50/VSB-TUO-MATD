from enum import Enum


class DepthFirstType(Enum):
    PRE_ORDER = 0
    IN_ORDER = 1
    POST_ORDER = 2


class TreeSearch(object):

    def __init__(self, tree):
        self._tree = tree

    def depth_first(self, callback, order=DepthFirstType.POST_ORDER):
        self._recursive_depth_first(order, self._tree, callback)

    def _recursive_depth_first(self, order, node, callback):
        if order == DepthFirstType.PRE_ORDER:
            callback(node)

        if node.left is not None:
            self._recursive_depth_first(order, node.left, callback)

        if order == DepthFirstType.IN_ORDER:
            callback(node)

        if node.right is not None:
            self._recursive_depth_first(order, node.right, callback)

        if order == DepthFirstType.POST_ORDER:
            callback(node)
