import unittest
from main import Node
from main import Node

class TestMain(unittest.TestCase):

    def test_lca(self):
        #test 1 - empty tree
        b_1 = Node(None)
        p = 1
        q = 2
        result = Node.lca(b_1, p, q)
        self.assertEqual(result, None)
        #test 2 - a tree which only has a root
        b_1 = Node(1)
        p = 1
        q = 2
        result = Node.lca(b_1, p, q)
        self.assertEqual(result, 1)
        #test 3 -  tree which is missing a value that is asked for
        p = 4
        b_1.left = Node(3)
        b_1.right = Node(2)
        result = Node.lca(b_1, p, q)
        self.assertEqual(result, 2) #if p found and q not (or vice-versa), it will return that value
        #test 4 - tree in which p is the root
        p = 1
        q = 2
        result = Node.lca(b_1, 1, 2)
        self.assertEqual(result, 1)
        #test 5 -  tree where p = q
        p = 2
        result = Node.lca(b_1, p, q)
        self.assertEqual(result, 2)
        #test 6 - where p is a parent of q
        p = 2
        q = 5
        b_1.right.right = Node(5)
        result = Node.lca(b_1, p ,q)
        self.assertEqual(result, 2)
        #tree which is valid but does NOT hold the values asked for
        p = 12
        q = 19
        result = Node.lca(b_1, p,q)
        self.assertEqual(result, None)



#if "__name__" == "__main__":
#    unittest.main()
