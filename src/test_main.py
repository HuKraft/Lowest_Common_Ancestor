import unittest
from main import Node

#the plan:  - create DAGs using dictionaries (easy).
#           - write a function that finds all the paths of a Node (path)
#           - write a funcion that compares those paths and finds (lca_dga)
#           the LCA by finding the node which is the closest parent
#           of both


class TestMain(unittest.TestCase):
#new tests - will delete old ones later - may still use them as templates
#some tests will differ as they would not make sense to create in the
#context of these new functions and the DGA type

    def test_path(self):

        #test 1 - finding a path which exists
        d = {1: [2, 3],
             2: [3, 4],
             3: [4],
             4: [3],
             5: [6],
             6: [3]}
        root = 1
        value = 4
        result = path(d, root, value, [])
        self.assertEqual(result, [[1, 2, 3, 4], [1, 2, 4], [1, 3, 4]])

        #test 2 - finding a path from a non-existent root to an existent value
        root = 7
        result = path(d, root, value, [])
        self.assertEqual(result, None)

        #test 3 - finding a pathfrom an existing root to a value which doesn't exist
        root = 1
        value = 7
        result = path(d, root, value, [])
        self.assertEqual(result, None)

        #test 4 - finding a path between the root and a value which is unreachable
        #(this is equivalent to test 3, but I'll do it to be in good form)
        d = {1: [2, 3],
             2: [3, 4],
             3: [4],
             4: [3],
             5: [6],
             6: [3],
             7: []}
        result = path(d, root, value, [])
        self.assertEqual(result, None)     

    def test_lca_dga(self):
        #test 1 - empty dga
        dga = {}
        p = 1
        q = 1
        result = lca_dga(dga, p, q, [])
        self.assertEqual(result, None)
        #test 2 - a graph which has one root that aims nowhere
        d = {1: None}
        p = 1
        q = 1
        result = lca_dga(d, p , q, [])
        self.assertEqual(result, None)
        #test 3 -  graph which is missing a value that is asked for
        d = {1: [2,3],
             2: [3,4,5],
             3: [],
             4: [],
             5: [4]}
        p = 7
        q = 1
        result = lca_dga(d, p, q, [])
        self.assertEqual(result, None)

#--------------------------------------------
    def test_lca(self):
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
