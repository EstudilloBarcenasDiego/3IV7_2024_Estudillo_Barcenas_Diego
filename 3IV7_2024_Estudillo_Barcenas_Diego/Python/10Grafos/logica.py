import heapq
def dijkastra(grafo, inicio):
    # Inicializar las distancias como infinito para todos los nodos
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0  # La distancia al nodo de inicio es 0
    cola_prioridad = [(0, inicio)]  # Cola de prioridad inicializada con el nodo de inicio

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # Iterar sobre los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            # Actualizar la distancia si encontramos un camino más corto
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias  # Aquí devolvemos las distancias
def kruskal(aristas, nodos):
    aristas = sorted(aristas, key=lambda x: x[2]) #ordenando por el peso
    padre = {nodo : nodo for nodo in nodos}
    def encontrar(nodo):
        if padre[nodo] != nodo:
            padre[nodo] = encontrar(padre[nodo])
        return padre[nodo]
    mst = []
    for u, v, peso in aristas:
        raiz_u = encontrar(u)
        raiz_v = encontrar(v)
        if raiz_u != raiz_v:
            mst.append((u, v, peso))
            padre[raiz_u] = raiz_v
    return mst