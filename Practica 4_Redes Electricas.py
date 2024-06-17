"""Dafne Villanueva 21310176
Algoritmo de Prim aplicado a la gestión de redes eléctricas:  proporciona un ejemplo básico de cómo el algoritmo de Prim
puede ser utilizado para optimizar la gestión de redes eléctricas, mostrando claramente la red original y el Árbol de Expansión
Mínima resultante."""



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

# Crear un grafo con networkx representando la red eléctrica
G = nx.Graph()

# Añadir nodos y aristas (subestaciones y líneas de transmisión con sus costos)
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'H', weight=8)
G.add_edge('B', 'H', weight=11)
G.add_edge('B', 'C', weight=8)
G.add_edge('C', 'I', weight=2)
G.add_edge('C', 'F', weight=4)
G.add_edge('C', 'D', weight=7)
G.add_edge('D', 'F', weight=14)
G.add_edge('D', 'E', weight=9)
G.add_edge('E', 'F', weight=10)
G.add_edge('F', 'G', weight=2)
G.add_edge('G', 'H', weight=1)
G.add_edge('G', 'I', weight=6)
G.add_edge('H', 'I', weight=7)

# Calcular el Árbol de Expansión Mínima usando el algoritmo de Prim
mst = prim_mst(G)

# Imprimir el resultado en la consola
print("Árbol de Expansión Mínima (MST):")
for from_node, to_node, weight in mst:
    print(f"Desde {from_node} hasta {to_node} con peso {weight}")

# Crear un nuevo grafo para el Árbol de Expansión Mínima
mst_graph = nx.Graph()
for from_node, to_node, weight in mst:
    mst_graph.add_edge(from_node, to_node, weight=weight)

# Visualizar la red eléctrica original y el Árbol de Expansión Mínima
pos = nx.spring_layout(G)  # Posiciones para los nodos

plt.figure(figsize=(14, 7))  # Tamaño de la figura

# Subplot 1: Red Eléctrica Original
plt.subplot(121)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)  # Dibujar el grafo original
labels = nx.get_edge_attributes(G, 'weight')  # Obtener etiquetas de las aristas
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Dibujar etiquetas de las aristas
plt.title("Red Eléctrica Original")  # Título del gráfico

# Subplot 2: Árbol de Expansión Mínima
plt.subplot(122)
nx.draw(mst_graph, pos, with_labels=True, node_color='lightgreen', node_size=500, font_size=10)  # Dibujar el MST
mst_labels = nx.get_edge_attributes(mst_graph, 'weight')  # Obtener etiquetas de las aristas del MST
nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=mst_labels)  # Dibujar etiquetas de las aristas del MST
plt.title("Árbol de Expansión Mínima")  # Título del gráfico

# Mostrar el gráfico
plt.show()  # Mostrar los gráficos
