import heapq

def dijkstra(grafo, origem, destino):
    custos = {cidade: float('inf') for cidade in grafo}
    custos[origem] = 0
    anteriores = {cidade: None for cidade in grafo}
    fila = [(0, origem)]

    while fila:
        custo_atual, atual = heapq.heappop(fila)
        if atual == destino:
            break

        for vizinho, custo in grafo[atual]:
            novo_custo = custo_atual + custo
            if novo_custo < custos[vizinho]:
                custos[vizinho] = novo_custo
                anteriores[vizinho] = atual
                heapq.heappush(fila, (novo_custo, vizinho))

    return custos, anteriores

def reconstruir_caminho(anteriores, destino):
    caminho = []
    while destino:
        caminho.insert(0, destino)
        destino = anteriores[destino]
    return caminho

# Grafo com cidades e custo das viagens (pedágio + combustível em reais)
grafo = {
    "Cidade A": [("Cidade B", 100), ("Cidade C", 150)],
    "Cidade B": [("Cidade A", 100), ("Cidade D", 120)],
    "Cidade C": [("Cidade A", 150), ("Cidade D", 80)],
    "Cidade D": [("Cidade B", 120), ("Cidade C", 80), ("Cidade E", 90)],
    "Cidade E": [("Cidade D", 90)]
}

# Definir origem e destino
origem = "Cidade A"
destino = "Cidade E"

# Executar o algoritmo
custos, anteriores = dijkstra(grafo, origem, destino)
caminho = reconstruir_caminho(anteriores, destino)

# Exibir resultado
print(f"Rota mais econômica de '{origem}' até '{destino}':")
print(" → ".join(caminho))
print(f"Custo total: R$ {custos[destino]:.2f}")
