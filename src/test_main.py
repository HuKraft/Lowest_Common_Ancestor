import unittest
from main import Node
from main import bintree

class TestMain(unittest.TestCase):

    def test_is_empty(self):
        #testing for a binary tree which only has a root -
        #no point testing for bintree with empty root: it would be the same
        t = bintree(1)
        self.assertTrue(bintree.is_empty(t))
        #testing for a binary tree which is non-empty
        t.root.left = 3
        self.assertFalse(bintree.is_empty(t))

    def test_tree_valid(self):#function which tests if a tree is valid (makes it robust)
        #empty tree
        b = bintree(None)
        result = bintree.tree_valid(b)
        self.assertTrue(result)
        #tree which is valid
        b = bintree(1)
        b.root.left = Node(5)
        b.root.right = Node(3)
        result = bintree.tree_valid(b)
        self.assertTrue(result)
        #invalid tree (has a value appear more than once)
        b.root.left.left = Node(5)
        result = bintree.tree_valid(b)
        self.assertFalse(result)
        #invalid tree (there exists a node that is not of type Node)
        b.root.left.right = 3
        result = bintree.tree_valid(b)
        self.assertFalse(result)
        return

    def test_lca(self):
        #test 1 - empty tree
        b_1 = bintree(None)
        p = 1
        q = 2
        result = bintree.lca(b_1, p, q)
        self.assertEqual(b_1, -1)
        #test 2 - a tree which only has a root
        b_1 = bintree(1)
        p = 1
        q = 2
        result = bintree.lca(b_1)
        self.assertEqual(result, -1)
        #test 3 -  tree which is missing a value that is asked for
        p = 4
        b_1.root.left = Node(3)
        b_1.root.right = Node(2)
        result = bintree.lca(b_1)
        self.assertEqual(result, -1)
        #test 4 - tree in which p is the root
        p=1
        result = bintree.lca(b_1)
        self.assertEqual(result, -1)
        #test 5 -  tree where p = q
        p = 1
        q = 1
        t = bintree(1)
        t.root.left = Node(2)
        t.root.right = Node(3)
        self.assertEqual(bintree.lca(t, p, q), 1)
        #testing for a tree in which p is a parent of q
        p = 5
        q = 2
        b_1.root.right.right = Node(5)
        result = bintree.lca(b_1)
        self.assertEqual(result, 1)



#if "__name__" == "__main__":
#    unittest.main()
