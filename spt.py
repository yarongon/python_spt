# %%
import networkx as nx

# %%
def find_spt(digraph, root):
    """
    Finding the shortest-path-tree
    See algorithm here:
    https://web.archive.org/web/20200124171216/http://www.me.utexas.edu/~jensen/exercises/mst_spt/spt_demo/spt1.html
    (Original link is dead: http://www.me.utexas.edu/~jensen/exercises/mst_spt/spt_demo/spt1.html)
    :param digraph: graph
    :param root: root node
    :return: spt
    """
    spt = nx.Graph()
    s1 = {root}
    s2 = set(digraph.nodes())
    s2.remove(root)
    while s2:
        nodes_from_s2_to_s1 = set()
        direct_reachable_nodes = []
        for source in s1:
            direct_reachable_nodes.extend(digraph.edges(source, data='weight'))

        direct_reachable_nodes = filter(lambda n1_n2_w: n1_n2_w[1] in s2, direct_reachable_nodes)
        smallest_weight_edge = min(direct_reachable_nodes, key=lambda n1_n2_w: n1_n2_w[2])
        spt.add_weighted_edges_from([smallest_weight_edge])
        nodes_from_s2_to_s1.add(smallest_weight_edge[1])
        s1.update(nodes_from_s2_to_s1)
        s2.difference_update(nodes_from_s2_to_s1)

    return spt

# %%
def draw_graph(G):
    import matplotlib.pyplot as plt
    edge_labels = {(n1, n2): d["weight"] for n1, n2, d in G.edges(data=True)}
    pos = nx.spring_layout(G)
    plt.figure()    
    nx.draw(G,pos, with_labels=True, node_size=500,node_color='pink')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
# %%
if __name__ == "__main__":
    G = nx.Graph()
    G.add_weighted_edges_from([
        (0, 1, 8),
        (0, 2, 5),
        (1, 2, 9),
        (1, 3, 11),
        (2, 3, 15),
        (2, 4, 10),
        (3, 4, 7)
    ])
    
    draw_graph(G)
    spt = find_spt(G, 0)
    draw_graph(spt)
    
# %%

# %%
