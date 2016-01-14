import networkx as nx


def find_spt(digraph, root):
    """
    Finding the shortest-path-tree
    See algorithm here:
    http://www.me.utexas.edu/~jensen/exercises/mst_spt/spt_demo/spt1.html
    :param digraph: graph
    :param root: root node
    :return: spt
    """
    spt = nx.Graph()
    s1 = set()
    s1.add(root)
    path_length = {root: 0}
    s2 = set(digraph.nodes())
    s2.remove(root)
    stop_flag = False
    while s2:
        nodes_from_s2_to_s1 = set()
        direct_reachable_nodes = []
        for source in s1:
            direct_reachable_nodes.extend(digraph.out_edges(source, data='weight'))

        direct_reachable_nodes = filter(lambda (n1, n2, data): n2 in s2, direct_reachable_nodes)
        smallest_weight_edge = min(direct_reachable_nodes, key=lambda (n1, n2, data): data)
        spt.add_weighted_edges_from([smallest_weight_edge])
        nodes_from_s2_to_s1.add(smallest_weight_edge[1])
        s1.update(nodes_from_s2_to_s1)
        s2.difference_update(nodes_from_s2_to_s1)

    return spt
