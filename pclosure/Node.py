class Node(object):

    def __init__(self, antecedent=None, closing=False):
        # The first node must be opening, otherwise the Node tree does not go beyond the depth of the first node.
        if antecedent != None and closing == False:
            raise Exception("Antecedent cannot be specified without also specifying whether the node is closing or not")

        self.parentheses = antecedent
        if closing:
            self.parentheses += ")"
        else:
            self.parentheses += "("

        self.closed = self.closed()
        self.descendants = []
        self.depth = 1

    def closed():
        # Check if this node's parenthetical statement is closed and complete
        opening_count = 0
        for i in range(len(self.parentheses)):
            if self.parentheses[i] == "(":
                opening_count += 1
            elif self.parentheses[i] == ")":
                opening_count -= 1

            if opening_count == 0 and i >= 1:
                self.closed = True
                return

        self.closed = False
        return

    def extend(depth):
        # Extends the depth of this node's descendants to the provided depth
        if len(self.descendants > 0):
            raise Exception("A node only needs to be extended once")
        if depth == 0:
            # A recursive escape statement
            return
        if not self.closed:
            self.descendants.append(Node(self, False))
            self.descendants.append(Node(self, True))
            for i in range(depth - 1):
                for descendant in self.descendants:
                    descendant.extend(i)
        self.depth = self.depth()

    def reduce(depth):
        # Reduces the depth of this node's descendants to the provided depth
        if depth <= 1:
            self.descendants = []
        for descendant in self.descendants:
            descendant.reduce(depth - 1)

    def closure_probability():
        probability_sum = 0
        probability = 1
        if len(self.descendants) == 0:
            if self.closed:
                return 1
            else:
                return 0
        for descendant in self.descendants:
            probability_sum += descendant.closure_probability() * 0.5
        return probability_sum

    def depth():
        depth = 1
        if len(self.descendants) == 0:
            return depth
        return depth + self.descendants[0].depth()
