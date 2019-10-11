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
        b = bintree(None)
        result = bintree.tree_list(b)
        self.assertEqual(result, [])
        #test 2 - testing to see if it creates the correct list
        b = bintree(1)
        b.root.left = Node(0)
        b.root.right = Node(5)
        result = bintree.tree_list(b)
        self.assertEqual(result, [1, 0, 5])
        #test 3 - testing to make sure it works on uneven tree
        b.root.left.left = Node(1)
        b.root.left.right = Node(3)
        b.root.left.left.left = Node(9)
        result = bintree.tree_list(b)
        self.assertEqual(result, [1, 0, 1, 0, 3, 5])
        #test 4 - testing when imbalanced on other side
        #(based on how I think I want my function to work
        t = binary(1)
        t.root.right = Node(2)
        t.root.right.left = Node(3)
        t.root.right.right= Node(4)
        result bintree.tree_list(t)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_tree_valid(self):#function which tests if a tree is valid (makes it robust)
        #empty tree
        b = bintree()
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
        #invalid tree (there exists a node that is not of type node)
        b.root.left.right = 3
        result = bintree.tree_valid(b)
        self.assertFalse(result)
        return

    def test_lca(self):
        #testing for an empty tree
        b_1 = binary(None)
        p = 1
        q = 2
        result = bintree.lca(b_1, p, q)
        self.assertRaises("")
        #testing for a tree which only has a root
        b_1 = binary(1)
        p = 1
        q = 2
        result = bintree.lca(b_1)
        self.assertEqual()
        #testing for tree which is missing a value that is asked for
        b_1 =
        #testing for a tree where p = q
        p = 1
        q = 1
        t = bintree(1)
        t.root.left = 2
        t.root.right = 3
        self.assertEqual(bintree.lca(t, p, q), 1)
        #testing for a tree in which p is a parent of q

#if "__name__" == "__main__":
#    unittest.main()
