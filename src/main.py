#add data structure

#add is_empty

#add search

#add blah blah

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class bintree(object):
    def __init__(self, root):
        self.root = Node(root)

    def is_empty(self):
        if isinstance(self, bintree):
            return (self.root.left == None and self.root.right == None)
        else:
            return (self.left == None and self.right == None)

    #def exists(self, x);
    #    return x in tree_list

    def tree_list(self):
        if isinstance(self, bintree):
            l = [self.root.value]
        else:
            l = [self.value]
        if not bintree.is_empty(self):
            return l + bintree.tree_list(self.root.left) + bintree.tree_list(self.root.right)
        else:
            return []

    def tree_valid(self):
        return 1


    def lca(t, p, q):
        return 1


#example of how to build a general binary tree
tree = bintree(2)
tree.root.left = Node(2)
tree.root.left = Node(3)
