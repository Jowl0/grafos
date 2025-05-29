import networkx as nx
import matplotlib.pyplot as plt
import grafos_tools as gt

plt.style.use("default")

aristas = [
    "A75D",
    "S14A",
    "S16B",
    "S13C",
    "S12D",
    "C29D",
    "B21C",
    "A27B",
    "A87E",
    "B86F",
    "C100G",
    "D75H",
    "H23G",
    "F22G",
    "E24F",
    "E81I",
    "F97J",
    "G83K",
    "H91L",
    "I12J",
    "J131K",
    "K16L",
]

vertices, index = gt.lista_vertices(aristas)

matrix = gt.matriz_adyacencia(aristas, vertices, index)


def prim(matriz, vertices):
    n = len(matriz)
    path = [False] * n
    path[0] = True
    arbol_minimo = []
    peso_min = 0
    while len(arbol_minimo) < n - 1:
        v1 = -1
        v2 = -1
        menor_peso = float("inf")
        for i in range(n):
            if path[i]:
                for j in range(n):
                    if not path[j] and matriz[i][j] < menor_peso:
                        menor_peso = matriz[i][j]
                        v1 = i
                        v2 = j

        path[v2] = True
        arbol_minimo.append(f"{vertices[v1]}{int(menor_peso)}{vertices[v2]}")
        peso_min += menor_peso

    return arbol_minimo, peso_min


arbol, pesomin = prim(matrix, vertices)

G = gt.dibujar_grafo(vertices, aristas)
H = gt.dibujar_grafo(vertices, arbol)


pos = nx.spring_layout(G, seed=42, k=1.5)

plt.figure(figsize=(12, 10))

nx.draw_networkx_nodes(G, pos, node_color="lightgrey", node_size=1000)
nx.draw_networkx_edges(G, pos, edge_color="lightgrey", width=2)
nx.draw_networkx_labels(G, pos, font_color="grey", font_size=14)

labels_grafo = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=labels_grafo, font_color="lightgrey", font_size=12
)

nx.draw_networkx_nodes(H, pos, node_color="#d8a8ff", node_size=1000)
nx.draw_networkx_edges(H, pos, edge_color="#7b42f6", width=4)
nx.draw_networkx_labels(H, pos, font_color="black", font_size=14)

labels_arbol = nx.get_edge_attributes(H, "weight")
nx.draw_networkx_edge_labels(
    H, pos, edge_labels=labels_arbol, font_color="#5c2bc5", font_size=12
)

plt.text(
    0.5,
    -0.2,
    f"Peso mínimo: {pesomin}",
    fontsize=10,
    ha="center",
    bbox=dict(facecolor="white", edgecolor="black", boxstyle="round,pad=0.5"),
    transform=plt.gca().transAxes,
)

plt.title("Árbol de peso minimo", fontsize=12)
plt.axis("off")
plt.tight_layout()
plt.show()
