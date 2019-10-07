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
        return (self.root.left == None and self.root.right == None)

tree = bintree(1)
tree.root.left = Node(1)
tree.root.left = Node(1)
