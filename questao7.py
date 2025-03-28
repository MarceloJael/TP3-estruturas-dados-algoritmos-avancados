import heapq

def prim(grafo, inicio):
    visitados = set()
    agm = []
    custo_total = 0
    fila = [(0, inicio, None)]  # (custo, bairro_atual, bairro_anterior)

    while fila:
        custo, atual, anterior = heapq.heappop(fila)
        if atual in visitados:
            continue

        visitados.add(atual)
        if anterior is not None:
            agm.append((anterior, atual, custo))
            custo_total += custo

        for vizinho, peso in grafo[atual]:
            if vizinho not in visitados:
                heapq.heappush(fila, (peso, vizinho, atual))

    return agm, custo_total

# Grafo com bairros e custo de instalação (em mil reais)
grafo = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("C", 5), ("D", 10)],
    "C": [("A", 2), ("B", 5), ("D", 3), ("E", 8)],
    "D": [("B", 10), ("C", 3), ("E", 7)],
    "E": [("C", 8), ("D", 7)]
}

# Executar algoritmo de Prim a partir do bairro A
agm, custo = prim(grafo, "A")

# Exibir resultado
print("Conexões escolhidas na Árvore Geradora Mínima:")
for origem, destino, peso in agm:
    print(f"{origem} ↔ {destino} (custo: R$ {peso} mil)")
print(f"\nCusto total mínimo: R$ {custo} mil")
