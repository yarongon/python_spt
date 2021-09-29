# %%
import networkx as nx
from networkx.algorithms.shortest_paths.weighted import single_source_dijkstra


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
    s2 = set(G.nodes())
    s2.remove(root)
    while s2:
        nodes_from_s2_to_s1 = set()
        direct_reachable_nodes = set()
        
        for _s in s1:
            for _i in digraph.adj[_s]:
                direct_reachable_nodes.add(_i)
            
        direct_reachable_nodes = direct_reachable_nodes - s1
        shortest_paths = [nx.single_source_dijkstra(digraph, source=root, target=t, weight="weight") for t in direct_reachable_nodes]
        shortest_path = min(shortest_paths)
        
        edge_to_add = (shortest_path[1][-2], shortest_path[1][-1], shortest_path[0])
        spt.add_weighted_edges_from([edge_to_add])
        nodes_from_s2_to_s1.add(shortest_path[1][-1])
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
        ('A', 'B', 1), ('A', 'F', 1), ('B', 'C', 1), ('B', 'G', 1), ('C', 'D', 1),
        ('C', 'H', 1), ('D', 'E', 1), ('D', 'I', 1), ('E', 'J', 1), ('F', 'G', 1),
        ('F', 'K', 1), ('G', 'H', 1), ('G', 'L', 1), ('H', 'I', 1), ('H', 'M', 1),
        ('I', 'J', 1), ('I', 'N', 1), ('J', 'O', 1), ('K', 'L', 1), ('K', 'P', 1),
        ('L', 'M', 1), ('L', 'Q', 1), ('M', 'N', 1), ('M', 'R', 1), ('N', 'O', 1),
        ('N', 'S', 1), ('O', 'T', 1), ('P', 'Q', 1), ('Q', 'R', 1), ('R', 'S', 1),
        ('S', 'T', 1)
    ])
    draw_graph(G)

    spt = find_spt(G, "K")
    draw_graph(spt)

# %%
