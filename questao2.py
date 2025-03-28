import heapq

def dijkstra(grafo, inicio, destino):
    dist = {v: float('inf') for v in grafo}
    dist[inicio] = 0
    anteriores = {v: None for v in grafo}
    fila = [(0, inicio)]

    while fila:
        tempo_atual, atual = heapq.heappop(fila)

        if atual == destino:
            break

        for vizinho, tempo in grafo[atual]:
            novo_tempo = tempo_atual + tempo
            if novo_tempo < dist[vizinho]:
                dist[vizinho] = novo_tempo
                anteriores[vizinho] = atual
                heapq.heappush(fila, (novo_tempo, vizinho))

    return dist, anteriores

def reconstruir_caminho(anteriores, destino):
    caminho = []
    while destino:
        caminho.insert(0, destino)
        destino = anteriores[destino]
    return caminho

# Grafo da cidade com tempo médio de deslocamento (em minutos)
grafo = {
    "Centro": [("Bairro A", 10), ("Bairro B", 15)],
    "Bairro A": [("Centro", 10), ("Bairro C", 12)],
    "Bairro B": [("Centro", 15), ("Bairro C", 10), ("Bairro D", 20)],
    "Bairro C": [("Bairro A", 12), ("Bairro B", 10), ("Bairro D", 5)],
    "Bairro D": [("Bairro B", 20), ("Bairro C", 5), ("Bairro E", 7)],
    "Bairro E": [("Bairro D", 7)]
}

# Definir origem e destino
inicio = "Centro"
destino = "Bairro E"

# Executar Dijkstra
distancias, anteriores = dijkstra(grafo, inicio, destino)
caminho = reconstruir_caminho(anteriores, destino)

# Exibir resultado
print(f"Trajeto mais rápido de '{inicio}' até '{destino}':")
print(" → ".join(caminho))
print(f"Tempo total: {distancias[destino]} minutos")