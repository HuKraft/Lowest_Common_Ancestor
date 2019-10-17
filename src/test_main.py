import unittest
from main import Node
from main import *
#the plan:  - create DAGs using dictionaries (easy).
#           - write a function that finds all the paths of a Node (path)
#           - write a funcion that compares those paths and finds (lca_dga)
#           the LCA by finding the node which is the closest parent
#           of both

class TestMain(unittest.TestCase):
#new tests - will delete old ones later - may still use them as templates
#some tests will differ as they would not make sense to create in the
#context of these new functions and the DGA type

    def test_has_key(self):#function which verifies that a given key is present
        #test 1 - key exists in dictionary
        d = {1: [2, 3],
             2: [3,4],
             3: [],
             4: [3]}
        key = 3
        result = has_key(d, key)
        self.assertTrue(result)
        #test 2 - key does not exist in dictionary
        key = 5
        result = has_key(d, key)
        self.assertFalse(result)

    def test_dag_path(self):

        #test 1 - finding a path which exists
        d = {1: [2, 3],
             2: [3, 4],
             3: [4],
             4: [5],
             5: []}
        root = 1
        value = 4
        result = dag_path(d, root, value, [])
        self.assertEqual(result, [[1, 2, 3, 4], [1, 2, 4], [1, 3, 4]])

        #test 2 - finding a path from a non-existent root to an existent value
        root = 7
        result = dag_path(d, root, value, [])
        self.assertEqual(result, [])

        #test 3 - finding a pathfrom an existing root to a value which doesn't exist
        root = 1
        value = 7
        result = dag_path(d, root, value, [])
        self.assertEqual(result, [])

        #test 4 - finding a path between the root and a value which is unreachable
        #(this is equivalent to test 3, but I'll do it to be in good form)
        d = {1: [2, 3],
             2: [3, 4],
             3: [4],
             4: [5],
             5: []}
        result = dag_path(d, root, value, [])
        self.assertEqual(result, [])

    def test_lca_dag(self):
        #test 1 - empty dga
        d = {}
        p = 1
        q = 2
        result = lca_dag(d, p , q)
        self.assertEqual(result, None)
        #test 2 - a graph which has one root that aims nowhere
        d = {1: None}
        p = 1
        q = 2
        result = lca_dag(d, p , q)
        self.assertEqual(result, None)
        #test 3 -  graph which is missing a value that is asked for
        d = {1: [2, 3],
             2: [4],
             3: [5,6],
             4: [],
             5: [],
             6: [5]}
        p = 7
        q = 3
        result = lca_dag(d, p, q, [])
        self.assertEqual(result, None)
        #test 4 - finding the LCA of p and q which each only have one path
        p = 6
        q = 2
        result = lca_dag(d, p, q, [])
        self.assertEqual(result, 1)
        #test 5 - finding the LCA of p and q, each of which have multiple paths
        #(but whose paths don't intersect)
        d = {1: [2,3],
             2: [4,5],
             3: [8,7],
             4: [6],
             5: [4],
             6: [],
             7: [8],
             8: [9],
             9: []}
        p = 4
        p = 8
        result = lca_dag(d, p , q)
        self.assertEqual(result, 1)
        #test 6 - finding the LCA where p is inside the path of q
        d = {1: [2, 3],
             2: [3, 4],
             3: [4, 5],
             4: [5],
             5: [6],
             6: []}
        p = 5
        q = 6
        result = lca_dag(d, p , q)
        self.assertEqual(result, 6)

#--------------------------------------------
"""
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
"""


#if "__name__" == "__main__":
#    unittest.main()
