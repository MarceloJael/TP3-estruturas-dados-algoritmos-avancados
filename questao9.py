import heapq

def prim(grafo, inicio):
    visitados = set()
    agm = []
    custo_total = 0
    fila = [(0, inicio, None)]  # (custo, cidade_atual, cidade_origem)

    while fila:
        custo, atual, origem = heapq.heappop(fila)
        if atual in visitados:
            continue

        visitados.add(atual)
        if origem is not None:
            agm.append((origem, atual, custo))
            custo_total += custo

        for vizinho, peso in grafo[atual]:
            if vizinho not in visitados:
                heapq.heappush(fila, (peso, vizinho, atual))

    return agm, custo_total

# Grafo com cidades e custo de transmissão (em milhões)
grafo = {
    "Cidade A": [("Cidade B", 6), ("Cidade C", 4)],
    "Cidade B": [("Cidade A", 6), ("Cidade C", 5), ("Cidade D", 10)],
    "Cidade C": [("Cidade A", 4), ("Cidade B", 5), ("Cidade D", 7), ("Cidade E", 8)],
    "Cidade D": [("Cidade B", 10), ("Cidade C", 7), ("Cidade E", 3)],
    "Cidade E": [("Cidade C", 8), ("Cidade D", 3)]
}

# Executar Prim a partir da Cidade A
agm, custo_total = prim(grafo, "Cidade A")

# Exibir resultado
print("Conexões escolhidas para expansão da rede elétrica:")
for origem, destino, custo in agm:
    print(f"{origem} ↔ {destino} (custo: R$ {custo} milhões)")

print(f"\nCusto total mínimo da rede: R$ {custo_total} milhões")