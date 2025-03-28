INF = float('inf')

def floyd_warshall(grafo, vertices):
    n = len(vertices)
    dist = [[INF] * n for _ in range(n)]

    # Inicializa com os pesos diretos
    for i in range(n):
        dist[i][i] = 0  # distância de um vértice para ele mesmo = 0

    for u in grafo:
        for v, peso in grafo[u]:
            i, j = vertices.index(u), vertices.index(v)
            dist[i][j] = peso

    # Algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Grafo com tempo de deslocamento entre bairros (em minutos)
grafo = {
    "A": [("B", 5), ("C", 10)],
    "B": [("A", 5), ("C", 3), ("D", 7)],
    "C": [("A", 10), ("B", 3), ("D", 1)],
    "D": [("B", 7), ("C", 1)]
}

vertices = ["A", "B", "C", "D"]
distancias = floyd_warshall(grafo, vertices)

# Exibir matriz de menores caminhos
print("Menor tempo de deslocamento entre todos os pares de bairros:\n")
print("   " + "  ".join(vertices))
for i, linha in enumerate(distancias):
    print(vertices[i], ["∞" if x == INF else x for x in linha])
