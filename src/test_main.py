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

    def test_exists(self): #testing for a function which makes sure a node exists
        #testing for trying to find a value in a binary which is totally is_empty
        #(not sure if I should add this node - depends on robustness wanted)
        b = bintree(None)
        value = 1
        exists(b, value)
        #if
    def test_lca(self):
        #testing for a tree which has takes the same two values (call them p and q)
        p = 1
        q = 1
        t = bintree(1)
        t.node.left = 2
        t.node.right = 3
        self.assertEqual(bintree.lca(t, p, q), 1)
        #more testing to add based on the robustness I'm looking for (will ask teacher)

#if "__name__" == "__main__":
#    unittest.main()
