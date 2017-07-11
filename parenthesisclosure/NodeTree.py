from parenthesisclosure import Node

class NodeTree(object):

    def __init__(self, depth):
        self.initialNode = Node()
        self.initialNode.extend(depth - 1)

    def extend(self, depth):
        self.initialNode.extend(depth)

    def closure_probability(self):
        return self.initialNode.closure_probability()
