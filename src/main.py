
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def lca(self, p, q):
        if self == None:
            return None
        left_lca = None
        right_lca = None
        if self.value == p or self.value == q:
            return self.value
        if self.left:
            left_lca = self.left.lca(p, q)
        if self.right:
            right_lca = self.right.lca( p, q)
        if left_lca and right_lca:
            return self.value
        return left_lca if left_lca else right_lca

b_1 = Node(1)
p = 1
q = 2
result = Node.lca(b_1, p, q)
print(result)
