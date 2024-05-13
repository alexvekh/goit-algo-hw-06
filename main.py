import networkx as nx
import matplotlib.pyplot as plt
from dfs_recursive import dfs_recursive
from collections import deque
from bfs_recursive import bfs_recursive
from dijkstra import dijkstra



G = nx.Graph()
G.add_nodes_from(['Home', 'Bus station A', 'Bus station B', 'Bus station C', 'Train station A', 'Train station B', 'Job'])
G.add_edges_from([('Home', 'Job'), 
                  ('Home', 'Bus station A'), 
                  ('Home', 'Train station A'), 
                  ('Bus station A', 'Bus station B'), 
                  ('Bus station B', 'Bus station C'),
                  ('Bus station C', 'Job'), 
                  ('Train station A', 'Train station B'), 
                  ('Train station B', 'Job')])

# ----  Завдання 1 ---------------------------
num_nodes = G.number_of_nodes()  # 4
num_edges = G.number_of_edges()  # 4
#  Ступінь центральності (Degree Centrality) визначається як кількість з'єднань, які має вузол.
degree_centrality = nx.degree_centrality(G)  # {'A': 0.6666666666666666, 'B': 1.0, 'C': 0.6666666666666666, 'D': 0.3333333333333333}
#  Близькість вузла (Closeness Centrality) визначається як обернене значення середньої відстані від вузла до всіх інших вузлів у графі.
closeness_centrality = nx.closeness_centrality(G)  # {'A': 0.75, 'B': 1.0, 'C': 0.75, 'D': 0.6}
# Посередництво вузла (Betweenness Centrality) визначається як кількість найкоротших шляхів між усіма парами вузлів, які проходять через даний вузол. Ця метрика відображає, наскільки вузол є "мостом" між іншими вузлами у графі.
betweenness_centrality = nx.betweenness_centrality(G)  # {'A': 0.0, 'B': 0.6666666666666666, 'C': 0.0, 'D': 0.0}

path = nx.shortest_path(G, source="Home", target="Job")  
avg_path_length = nx.average_shortest_path_length(G)  # NetworkXError: Graph is not strongly connected.

print(f"\nУ цьому графі {num_nodes} вешин і {num_edges} ребер") #is_connected)
print(f'\nСтупінь центральності:\n', degree_centrality)
print('\nБлизькість вузла:\n', closeness_centrality)
print('\nПосередництво вузла:\n', betweenness_centrality)
print("\nНайкоротший шлях: ", path)
print("\nСередня довжина шляху: ", avg_path_length)


print('\n    ----    Завдання 2    ---------------------------')
# DFS
dfs_tree = nx.dfs_tree(G, source='Home')
print("\nDFS_tree:", list(dfs_tree.edges()))  # виведе ребра DFS-дерева з коренем у вузлі A
print("Порядок перевірки вершин", list(dfs_tree.nodes()))
# BFS
bfs_tree = nx.bfs_tree(G, source='Home')
print("\nBFS_tree:", list(bfs_tree.edges()))  # виведе ребра BFS-дерева з коренем у вузлі A
print("Порядок перевірки вершин", list(bfs_tree.nodes()))

print("Порядо перевірки вершин алгоритмом DFS:")
print("\nАлгоритм DFS:", dfs_recursive(G, "Home"))
print("Порядо перевірки вершин алгоритмом BFS:")
print("\nАлгоритм BFS:", bfs_recursive(G, deque(["Home"])))

print('\n    ----    Завдання 3    ---------------------------')

G["Home"]["Job"]["weight"] = 17
G["Home"]["Bus station A"]["weight"] = 5
G["Home"]["Train station A"]["weight"] = 7
G["Bus station A"]["Bus station B"]["weight"] = 5
G["Bus station B"]["Bus station C"]["weight"] = 5
G["Bus station C"]["Job"]["weight"] = 5
G["Train station A"]["Train station B"]["weight"] = 2
G["Train station B"]["Job"]["weight"] = 5

# print(G["Home"]['Job']['weight'])
print("\nАлгоритм Дейкстри:", dijkstra(G, "Home"))
# ----  Візуалізація ---------------------------

labels = nx.get_edge_attributes(G, 'weight')
node_colors = ['red' if node in ['Train station A', 'Train station B'] else ('green' if node in ['Bus station A', 'Bus station B', 'Bus station C'] else 'lightblue') for node in G.nodes]  # Example coloring
node_sizes = 2000  # Set all nodes to size 600
edge_colors = ['red' if 'Train station A' and 'Train station B' in edge else ('green' if 'Bus station B' in edge else 'blue') for edge in G.edges]

edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)} 

pos = {
  'Home': (4, 4.25),
  'Job': (3.5, -0.5),
  'Train station A': (4.5, 4.5),
  'Train station B': (3, 0),
  'Bus station A': (3.5, 3.5),
  'Bus station B': (4, 2),
  'Bus station C': (4.5, 0.5),
}

options = {"node_color": node_colors, 
           "node_size": node_sizes, 
           "edge_color": edge_colors, 
           "pos": pos, 
           "with_labels": True, 
           "width": 3, 
           "alpha": 0.7,
           'label': edge_labels
           }

nx.draw(G, **options)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()