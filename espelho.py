import numpy as np

def espelhar_cubo(vertices):
    matriz_espelhamento = np.array([[-1, 0, 0],
                                   [0, -1, 0],
                                   [0, 0, -1]])

    vertices_espelhados = []

    for vertice in vertices:
        vertice_espelhado = np.dot(matriz_espelhamento, vertice)
        vertices_espelhados.append(vertice_espelhado)

    return vertices_espelhados

# Exemplo de coordenadas dos vértices do cubo
vertices_cubo = [np.array([0, 0, 0]),   # Vértice 0
                 np.array([1, 0, 0]),   # Vértice 1
                 np.array([0, 1, 0]),   # Vértice 2
                 np.array([1, 1, 0]),   # Vértice 3
                 np.array([0, 0, 1]),   # Vértice 4
                 np.array([1, 0, 1]),   # Vértice 5
                 np.array([0, 1, 1]),   # Vértice 6
                 np.array([1, 1, 1])]   # Vértice 7

# Chamando a função para espelhar o cubo
vertices_espelhados = espelhar_cubo(vertices_cubo)

# Imprimindo as coordenadas dos vértices espelhados
for i, vertice in enumerate(vertices_espelhados):
    print(f"Vértice {i}: {vertice}")
