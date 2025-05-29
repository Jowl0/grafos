import networkx as nx
import matplotlib.pyplot as plt
import grafos_tools as gt

aristas = {
    "S14A",
    "A29B",
    "S12D",
    "S16B",
    "S13C",
    "B21C",
    "C29D",
    "A87E",
    "B86F",
    "C100G",
    "D75H",
    "E24F",
    "F22G",
    "G23H",
    "E81I",
    "F97J",
    "G83K",
    "H91L",
    "I12J",
    "J131K",
    "K16L",
    "S75L",
}

vertices, index = gt.lista_vertices(aristas)
aristas_ordenadas = gt.ordenar_aristas(aristas)


def kruskall(aristas):
    aristas_kruskall = []
    conjuntos = []
    peso_min = 0
    for arista in aristas:
        u, v = gt.extraer_vertices(arista)

        conjunto_u = None
        conjunto_v = None
        for c in conjuntos:
            if u in c:
                conjunto_u = c
            if v in c:
                conjunto_v = c

        if conjunto_u is None and conjunto_v is None:
            conjuntos.append({u, v})
            aristas_kruskall.append(arista)

        elif conjunto_u is not None and conjunto_v is None:
            conjunto_u.add(v)
            aristas_kruskall.append(arista)

        elif conjunto_u is None and conjunto_v is not None:
            conjunto_v.add(u)
            aristas_kruskall.append(arista)

        elif conjunto_u != conjunto_v:
            conjunto_u.update(conjunto_v)
            conjuntos.remove(conjunto_v)
            aristas_kruskall.append(arista)

        else:
            pass
    for arista in aristas_kruskall:
        peso_min += gt.extraer_peso(arista)

    return aristas_kruskall, peso_min


arbol, pesomin = kruskall(aristas_ordenadas)
G = gt.dibujar_grafo(vertices, aristas_ordenadas)

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
