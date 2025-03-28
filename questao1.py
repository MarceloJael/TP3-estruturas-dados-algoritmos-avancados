import heapq

# Algoritmo de Dijkstra
def dijkstra(grafo, inicio):
    distancias = {v: float('inf') for v in grafo}
    distancias[inicio] = 0
    fila = [(0, inicio)]
    anteriores = {v: None for v in grafo}

    while fila:
        dist_atual, atual = heapq.heappop(fila)

        for vizinho, peso in grafo[atual]:
            nova_dist = dist_atual + peso
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                anteriores[vizinho] = atual
                heapq.heappush(fila, (nova_dist, vizinho))

    return distancias, anteriores

# Reconstruir o menor caminho
def reconstruir_caminho(anteriores, destino):
    caminho = []
    while destino:
        caminho.insert(0, destino)
        destino = anteriores[destino]
    return caminho

# Grafo com bairros e distâncias
grafo = {
    "Centro": [("A", 4), ("B", 2)],
    "A": [("Centro", 4), ("C", 3)],
    "B": [("Centro", 2), ("C", 1), ("D", 7)],
    "C": [("A", 3), ("B", 1), ("D", 2)],
    "D": [("B", 7), ("C", 2), ("E", 1)],
    "E": [("D", 1)]
}

# Executar Dijkstra a partir do "Centro"
distancias, anteriores = dijkstra(grafo, "Centro")

# Exibir resultados
print("Menores distâncias a partir do Centro:")
for bairro in grafo:
    print(f"- {bairro}: {distancias[bairro]} km")

print("\nMenores caminhos a partir do Centro:")
for bairro in grafo:
    caminho = reconstruir_caminho(anteriores, bairro)
    print(f"- {bairro}: {' → '.join(caminho)}")
