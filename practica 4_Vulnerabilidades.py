""" Dafne Villanueva 21310176
Algoritmo de Árbol Parcial Mínimo de Prim enfocado en la "Evaluación de Vulnerabilidades", donde identificamos los caminos más cortos
y potencialmente más vulnerables que un atacante podría utilizar para acceder a nodos críticos en una red,"""

import matplotlib.pyplot as plt
import networkx as nx

# Función para encontrar el Árbol de Expansión Mínima (MST) usando el algoritmo de Prim
def prim_mst(graph, start_node):
    visited = {node: False for node in graph}
    mst_edges = []
    min_heap = [(0, start_node)]  # Cola de prioridad para almacenar los bordes mínimos

    while min_heap:
        weight, node = min_heap.pop(0)  # Extraer el borde mínimo
        if visited[node]:
            continue
        visited[node] = True
        for neighbor, edge_weight in graph[node].items():
            if not visited[neighbor]:
                min_heap.append((edge_weight, neighbor))
        min_heap.sort()  # Ordenar la cola de prioridad después de agregar nuevos bordes
        mst_edges.append((node, neighbor, edge_weight))  # Añadir el borde al MST

    return mst_edges

# Grafo representando una red con nodos y pesos
graph = {
    'A': {'B': 1, 'C': 4, 'E': 7},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3, 'E': 5},
    'D': {'B': 6, 'C': 3, 'E': 1},
    'E': {'A': 7, 'C': 5, 'D': 1}
}

# Calcular el Árbol de Expansión Mínima (MST) usando el algoritmo de Prim
mst_edges = prim_mst(graph, 'A')

# Mostrar el grafo original
plt.figure(figsize=(12, 6))
plt.subplot(121)
G = nx.Graph()
for node in graph:
    for neighbor, weight in graph[node].items():
        G.add_edge(node, neighbor, weight=weight)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Grafo Original')

# Mostrar el Árbol de Expansión Mínima (MST)
plt.subplot(122)
MST = nx.Graph()
for edge in mst_edges:
    MST.add_edge(edge[0], edge[1], weight=edge[2])
pos_mst = nx.spring_layout(MST)
nx.draw(MST, pos_mst, with_labels=True, node_color='lightgreen', node_size=500, font_size=10)
nx.draw_networkx_edge_labels(MST, pos_mst, edge_labels={edge[:2]: edge[2] for edge in mst_edges})
plt.title('Árbol de Expansión Mínima (MST)')

# Mostrar ambas gráficas
plt.tight_layout()
plt.show()
