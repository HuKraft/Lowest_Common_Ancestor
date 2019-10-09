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

    def test_tree_list(self): #testing for a function which creates a list from the
        #elements of a binary tree. I will then use this to make sure the Node
        #that of which the lca is being looked for exists
        #test 1 - testing to see if it returns an empty list if the binary tree is is_empty
        #test 2 - testing to see if it creates the correct list
        b = bintree(1)
        b.root.left = Node(0)
        b.root.right = Node(5)
        result = bintree.tree_list(b)
        self.assertEqual(result, [1, 0, 4])
        #test 3 - testing to make sure it works on uneven tree
    def test_lca(self):
        #testing for a tree which has takes the same two values (call them p and q)
        p = 1
        q = 1
        t = bintree(1)
        t.root.left = 2
        t.root.right = 3
        self.assertEqual(bintree.lca(t, p, q), 1)
        #more testing to add based on the robustness I'm looking for (will ask teacher)

#if "__name__" == "__main__":
#    unittest.main()
