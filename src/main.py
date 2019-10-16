#add data structure

#add is_empty

#add search

#add blah blah


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_empty(self):
        return (self.value == None)
    def is_empty_root(self):
        return (self.left == None) and (self.right == None)

    def tree_valid_list(self):
        if self == None:
            return []
        return [self.value] + self.left.tree_valid_list() + self.right.tree_valid_list()

    def tree_valid(self, p, q):
        if ((not p in tree_valid_list) or (not q in tree_valid_list)):
            return False
        return True

    def lca(self, p, q):
        if self is None:
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

    def lca_t(self,p,q):
        if not self.tree_valid(p,q):
            return None
        return self.lca(p,q)
        return 1;

t = Node(2)
t.left = Node(3)
t.right = Node(4)
print(t.lca(5,6))
