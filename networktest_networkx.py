import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nodes = ['A1 - gather requirements','B2 - collect NFRs','C1 - document output', \
                  'D3 - deploy final output']
G.add_nodes_from(nodes)
G.add_edge(nodes[0],nodes[1])
G.add_edge(nodes[1],nodes[2])
G.add_edge(nodes[2],nodes[3])
G.add_edge(nodes[1],nodes[3])

pos={nodes[0]:(0,0), nodes[1]:(-1,3), nodes[2]:(2,0.5), nodes[3]:(4,1.5)}

nx.draw_networkx_nodes(G, pos, node_size=600, node_color='white', alpha=0.4, \
                       node_shape='o', margins=0.1,edgecolors='red')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
nx.draw_networkx_edges(G, pos, width=1, alpha=0.5, edge_color='blue')
nx.draw_networkx_edge_labels(G, pos, edge_labels={ (nodes[0],nodes[1]): 'A1-B2', \
    (nodes[1],nodes[2]): 'B2-C1', (nodes[2],nodes[3]): 'C1-D3', (nodes[1],nodes[3]): 'B2-D3'})
#nx.draw(G, with_labels=True)
plt.show()