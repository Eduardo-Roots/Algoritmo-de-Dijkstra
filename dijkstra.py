# -*- coding: utf-8 -*-

from collections import deque


def dijkstra(graph, vertex):
    queue = deque([vertex])
    distance = {vertex: 0}
    while queue:
        t = queue.popleft()
        print("\nEstamos visitando o nó " + str(t))
        for vizinho in graph[t]:
            queue.append(vizinho)
            new_distance = distance[t] + graph[t][vizinho]
            if (vizinho not in distance or new_distance < distance[vizinho]):
                distance[vizinho] = new_distance
                print(f'\tAtualizando o nó {str(vizinho)} com a distância : {str(new_distance)}')

    return distance


# Lista de adjacência do grafo
graph = {'A': {'B': 15, 'C': 4}, 'B': {'E': 5}, 'C': {'E': 11, 'D': 2}, 'D': {'E': 3}, 'E': {}}
distance = dijkstra(graph, 'A')
print("\n\nDistancias: " + str(distance))
