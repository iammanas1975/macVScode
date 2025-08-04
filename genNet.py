import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load Excel data
df = pd.read_excel("/Volumes/Transcend/Articles and Notes/DevOpsConsultFramework/New2025/questionnaire.xlsx", sheet_name="Sheet1")

# Create directed graph
G = nx.DiGraph()

# Add nodes with labels
for _, row in df.iterrows():
    task = row['Task no.']
    label = f"{row['Activity']}\n({task}, {row['Tool']}, {row['Role']})"
    G.add_node(task, label=label, trans_type=row['TransType'], time=row['Time'])

# Add edges based on predecessor columns
for _, row in df.iterrows():
    curr_task = row['Task no.']
    for pred_col in ['Pred 1', 'Pred 2', 'Pred 3']:
        pred = row[pred_col]
        if pd.notna(pred):
            edge_label = f"{row['TransType']}, {row['Time']}h"
            G.add_edge(pred, curr_task, label=edge_label, weight=row['Time'])

# Compute all paths ending at nodes with TransType C-C
end_nodes = [n for n, d in G.nodes(data=True) if d.get('trans_type') == 'C-C']
all_paths = []
for target in end_nodes:
    for path in nx.all_simple_paths(G, source='A1', target=target):
        time = sum(G[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
        all_paths.append((path, time))

# Identify critical path: longest time and ends in C-C
critical_path, max_time = max(all_paths, key=lambda x: x[1])

# Draw the network
plt.figure(figsize=(20, 12))
pos = nx.spring_layout(G, seed=42)

# Draw nodes
node_labels = nx.get_node_attributes(G, 'label')
nx.draw(G, pos, node_color='skyblue', node_size=3000, with_labels=False)
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)

# Draw edges
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)
nx.draw_networkx_edges(G, pos)

# Highlight critical path
edge_path = list(zip(critical_path[:-1], critical_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=edge_path, edge_color='red', width=2)

# Annotate critical path
plt.title(f"Critical Path (Red Edges) - Total Time: {max_time}h", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.savefig("/Volumes/Transcend/Articles and Notes/DevOpsConsultFramework/New2025/network_graph.pdf", format="PDF")
plt.show()