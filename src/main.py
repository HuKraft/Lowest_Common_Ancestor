
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def lca(self, p, q):
        if self == None:
            return None
        left_lca = None
        right_lca = None
        if self.value == p or self.value == q:
            return self.value
        if self.left:
            left_lca = self.left.lca(p, q)
        if self.right:
            right_lca = self.right.lca( p, q)
        if left_lca and right_lca:
            return self.value
        return left_lca if left_lca else right_lca


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def has_key(self,  key):
    if key in self.keys():
        return 1
    return 0;

def dag_path(graph, start, end, path=[]):
    return 1

def lca_dag(d, p, q):

    return 1


d = {1: [2, 3],
     2: [3, 4],
     3: [4],
     4: [5],
     5: []}
#print(dag_path(d, 1, 5, []))
