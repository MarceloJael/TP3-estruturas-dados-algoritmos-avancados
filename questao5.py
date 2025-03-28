import heapq

def dijkstra_com_autonomia(grafo, recarga, inicio, destino, autonomia_maxima):
    fila = [(0, inicio, 0, [])]  # (tempo_total, nó_atual, distância_acumulada, caminho)
    visitado = {}

    while fila:
        tempo, atual, distancia, caminho = heapq.heappop(fila)

        if (atual in visitado) and (visitado[atual] <= distancia):
            continue
        visitado[atual] = distancia

        caminho = caminho + [atual]

        if atual == destino:
            return caminho, tempo

        for vizinho, tempo_via, distancia_via in grafo[atual]:
            nova_distancia = distancia + distancia_via

            # Se passar da autonomia e não tiver estação, ignora
            if nova_distancia > autonomia_maxima and atual not in recarga:
                continue

            # Se tiver estação de recarga, zera autonomia
            nova_distancia = 0 if atual in recarga else nova_distancia

            heapq.heappush(fila, (tempo + tempo_via, vizinho, nova_distancia, caminho))

    return None, float('inf')

# Grafo: nó -> [(vizinho, tempo, distância)]
grafo = {
    "A": [("B", 5, 4), ("C", 10, 6)],
    "B": [("A", 5, 4), ("D", 7, 5)],
    "C": [("A", 10, 6), ("D", 3, 3)],
    "D": [("B", 7, 5), ("C", 3, 3), ("E", 6, 4)],
    "E": [("D", 6, 4), ("F", 4, 2)],
    "F": [("E", 4, 2)]
}

# Estações de recarga nos nós
estacoes_recarga = {"C", "E"}

# Entrada do usuário
inicio = "A"
destino = "F"
autonomia = 7  # autonomia em km

# Executar algoritmo
caminho, tempo_total = dijkstra_com_autonomia(grafo, estacoes_recarga, inicio, destino, autonomia)

# Exibir resultado
if caminho:
    print(f"Melhor rota de '{inicio}' até '{destino}': {' → '.join(caminho)}")
    print(f"Tempo total estimado: {tempo_total} min")
else:
    print("Não foi possível encontrar uma rota viável com a autonomia fornecida.")
