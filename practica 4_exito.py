"""Dafne Vilanueva  21310176
Algoritmo de Prim en el contexto de "calcular la ruta más corta al éxito".
El enfoque se basa en encontrar el Árbol de Expansión Mínima (MST) para identificar el camino de menor "costo" (o esfuerzo)
a través de diferentes etapas hacia el éxito."""

import heapq  # Para la implementación de la cola de prioridad
import matplotlib.pyplot as plt  # Para la visualización gráfica
import networkx as nx  # Para la creación y manipulación del grafo

# Función para implementar el algoritmo de Prim
def prim_mst(graph):
    mst = []  # Lista para almacenar el árbol de expansión mínima
    visited = set()  # Conjunto para rastrear los nodos visitados
    # Cola de prioridad para seleccionar la arista de menor peso
    min_heap = [(0, None, list(graph.nodes)[0])]  # (peso, desde_nodo, hasta_nodo)

    while min_heap:
        cost, from_node, to_node = heapq.heappop(min_heap)  # Selecciona la arista de menor peso
        
        if to_node in visited:  # Si el nodo ya fue visitado, saltarlo
            continue
        
        visited.add(to_node)  # Marcar el nodo como visitado
        
        if from_node is not None:  # Si no es el nodo inicial
            mst.append((from_node, to_node, cost))  # Añadir la arista al árbol de expansión mínima
        
        # Explorar los vecinos del nodo actual
        for next_node, edge_data in graph[to_node].items():
            if next_node not in visited:
                heapq.heappush(min_heap, (edge_data['weight'], to_node, next_node))  # Añadir arista a la cola de prioridad
    
    return mst  # Devolver el árbol de expansión mínima

# Crear un grafo con networkx representando las diferentes etapas hacia el éxito y sus costos
G = nx.Graph()

# Añadir nodos y aristas (etapas y sus costos)
G.add_edge('Inicio', 'Primer Paso', weight=2)
G.add_edge('Inicio', 'Motivación', weight=1)
G.add_edge('Primer Paso', 'Desafío Inicial', weight=3)
G.add_edge('Motivación', 'Planificación', weight=2)
G.add_edge('Desafío Inicial', 'Persistencia', weight=4)
G.add_edge('Planificación', 'Ejecutar Plan', weight=2)
G.add_edge('Persistencia', 'Crecimiento', weight=2)
G.add_edge('Ejecutar Plan', 'Crecimiento', weight=3)
G.add_edge('Crecimiento', 'Éxito', weight=1)
G.add_edge('Ejecutar Plan', 'Éxito', weight=5)

# Calcular el Árbol de Expansión Mínima usando el algoritmo de Prim
mst = prim_mst(G)

# Imprimir el resultado en la consola
print("Árbol de Expansión Mínima (MST) para calcular la ruta más corta al éxito:")
for from_node, to_node, weight in mst:
    print(f"Desde {from_node} hasta {to_node} con costo {weight}")

# Crear un nuevo grafo para el Árbol de Expansión Mínima
mst_graph = nx.Graph()
for from_node, to_node, weight in mst:
    mst_graph.add_edge(from_node, to_node, weight=weight)

# Visualizar el camino hacia el éxito y el Árbol de Expansión Mínima
pos = nx.spring_layout(G)  # Posiciones para los nodos

plt.figure(figsize=(14, 7))  # Tamaño de la figura

# Subplot 1: Camino Original hacia el Éxito
plt.subplot(121)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)  # Dibujar el grafo original
labels = nx.get_edge_attributes(G, 'weight')  # Obtener etiquetas de las aristas
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Dibujar etiquetas de las aristas
plt.title("Camino Original hacia el Éxito")  # Título del gráfico

# Subplot 2: Árbol de Expansión Mínima
plt.subplot(122)
nx.draw(mst_graph, pos, with_labels=True, node_color='lightgreen', node_size=500, font_size=10)  # Dibujar el MST
mst_labels = nx.get_edge_attributes(mst_graph, 'weight')  # Obtener etiquetas de las aristas del MST
nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=mst_labels)  # Dibujar etiquetas de las aristas del MST
plt.title("Árbol de Expansión Mínima para la Ruta al Éxito")  # Título del gráfico

# Mostrar el gráfico
plt.show()  # Mostrar los gráficos
