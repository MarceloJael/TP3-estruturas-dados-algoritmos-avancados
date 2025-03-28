import heapq

def dijkstra(grafo, origem, destino):
    dist = {v: float('inf') for v in grafo}
    dist[origem] = 0
    anteriores = {v: None for v in grafo}
    fila = [(0, origem)]

    while fila:
        atual_dist, atual = heapq.heappop(fila)
        if atual == destino:
            break

        for vizinho, peso in grafo[atual]:
            nova_dist = atual_dist + peso
            if nova_dist < dist[vizinho]:
                dist[vizinho] = nova_dist
                anteriores[vizinho] = atual
                heapq.heappush(fila, (nova_dist, vizinho))

    return dist, anteriores

def reconstruir_caminho(anteriores, destino):
    caminho = []
    while destino:
        caminho.insert(0, destino)
        destino = anteriores[destino]
    return caminho

# Grafo com aeroportos e distâncias diretas (em km)
grafo = {
    "Aeroporto A": [("Aeroporto B", 400), ("Aeroporto C", 600)],
    "Aeroporto B": [("Aeroporto A", 400), ("Aeroporto D", 350)],
    "Aeroporto C": [("Aeroporto A", 600), ("Aeroporto D", 200)],
    "Aeroporto D": [("Aeroporto B", 350), ("Aeroporto C", 200), ("Aeroporto E", 300)],
    "Aeroporto E": [("Aeroporto D", 300)]
}

# Definir origem e destino
origem = "Aeroporto A"
destino = "Aeroporto E"

# Executar Dijkstra
distancias, anteriores = dijkstra(grafo, origem, destino)
caminho = reconstruir_caminho(anteriores, destino)

# Exibir resultado
print(f"Melhor rota de '{origem}' até '{destino}':")
print(" → ".join(caminho))
print(f"Distância total: {distancias[destino]} km")