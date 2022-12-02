from Day_0 import get_day_input
import networkx as nx

G = nx.Graph()

for relations in get_day_input(12).strip().split('\n'): 
    origin, _, *destinations = relations.replace(',', '').split()
    G.add_edges_from([(origin, i) for i in destinations])

print(f"Day 12-1: {len(nx.shortest_path(G, '0'))}") # 169
print(f"Day 12-2: {len(list(nx.connected_component_subgraphs(G)))}") # 179