import unittest
from main import Node
from main import Node

class TestMain(unittest.TestCase):

    def test_is_empty(self):
        #testing for a binary tree which only has a root -
        #no point testing for Node with empty root: it would be the same
        t = Node(1)
        self.assertTrue(Node.is_empty(t))
        #testing for a binary tree which is non-empty
        t.left = 3
        self.assertFalse(Node.is_empty(t))

    def test_tree_valid(self):#function which tests if a tree is valid (makes it robust)
        #empty tree
        b = Node(None)
        p = 3
        q = 5
        result = Node.tree_valid(b, p, q, [])
        self.assertTrue(result)
        #tree which is valid and holds the values asked for
        b = Node(1)
        p = 3
        q = 5
        b.left = Node(5)
        b.right = Node(3)
        result = Node.tree_valid(b, p, q, [])
        self.assertTrue(result)
        #tree which is valid but does NOT hold the values asked for
        p = 12
        q = 5
        result = Node.tree_valid(b, p, q, [])
        self.assertFalse(result)
        #invalid tree (has a value appear more than once)
        b.left.left = Node(5)
        result = Node.tree_valid(b, p, q, [])
        self.assertFalse(result)
        #invalid tree (there exists a node that is not of type Node)
        b.left.right = 3
        result = Node.tree_valid(b, p, q, [])
        self.assertFalse(result)
        return

    def test_lca(self):
        #test 1 - empty tree
        b_1 = Node(None)
        p = 1
        q = 2
        result = Node.lca(b_1, p, q)
        self.assertEqual(b_1, -1)
        #test 2 - a tree which only has a root
        b_1 = Node(1)
        p = 1
        q = 2
        result = Node.lca(b_1, p, q)
        self.assertEqual(result, -1)
        #test 3 -  tree which is missing a value that is asked for
        p = 4
        b_1.left = Node(3)
        b_1.right = Node(2)
        result = Node.lca(b_1)
        self.assertEqual(result, -1)
        #test 4 - tree in which p is the root
        p=1
        result = Node.lca(b_1)
        self.assertEqual(result, -1)
        #test 5 -  tree where p = q
        p = 1
        q = 1
        t = Node(1)
        t.left = Node(2)
        t.right = Node(3)
        self.assertEqual(Node.lca(t, p, q), 1)
        #testing for a tree in which p is a parent of q
        p = 5
        q = 2
        b_1.right.right = Node(5)
        result = Node.lca(b_1)
        self.assertEqual(result, 1)



#if "__name__" == "__main__":
#    unittest.main()
