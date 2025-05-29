import networkx as nx
import numpy as np


def extraer_vertices(aristas_n):
    return aristas_n[0], aristas_n[-1]


def lista_vertices(aristas_n):
    vertices = set()
    for arista in aristas_n:
        vertice_1, vertice_2 = extraer_vertices(arista)
        vertices.add(vertice_1)
        vertices.add(vertice_2)

    vertices = list(vertices)
    indice = {v: i for i, v in enumerate(vertices)}
    return vertices, indice


def ordenar_aristas(aristas_n):
    lista_ordenada = sorted(aristas_n, key=lambda x: extraer_peso(x))
    return lista_ordenada


def extraer_peso(arista_n):
    return int(arista_n[1:-1])


def matriz_adyacencia(aristas, vertices, indice):
    n = len(vertices)
    matrix = np.full((n, n), float("inf"))  # Crear matriz n x n llena de inf

    for i in range(n):
        matrix[i, i] = 0

    for arista in aristas:
        v1, v2 = extraer_vertices(arista)
        peso = extraer_peso(arista)
        matrix[indice[v1], indice[v2]] = peso
        matrix[indice[v2], indice[v1]] = peso

    return matrix


def dibujar_grafo(vertices, aristas):
    G = nx.Graph()
    for vertice in vertices:
        G.add_node(vertice)

    for arista in aristas:
        u, v = extraer_vertices(arista)
        peso = extraer_peso(arista)
        G.add_edge(u, v, weight=peso)
    return G
