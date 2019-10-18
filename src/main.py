
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

#algorithm gotten from : https://www.python.org/doc/essays/graphs/
def dag_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not has_key(graph, start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = dag_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def lca_dag(d, p, q):
    if p not in d or q not in d:
        return None
    lst = []
    root = next(iter(d))
    p_list = dag_path(d, root, p, [])
    q_list = dag_path(d, root, q, [])
    for i in p_list:
        for j in q_list:
            lst.append([value for value in i if value in j])
    true_list = max(lst, key = len)
    return true_list[-1]


    return 1
