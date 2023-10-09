import heapq
from collections import defaultdict
from typing import List, Dict

def findShortestPath(n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
    # create adjacency list from input
    adjacency_list = defaultdict(list)

    for source, destination, weight in edges:
        adjacency_list[source].append([destination, weight])
        adjacency_list[destination].append([source, weight])
    
    # iterate through edges and use Dijkstra's algorithm
    shortest = {v: float('inf') for v in adjacency_list.keys()}           # vertex: distance
    shortest[src] = 0
    minHeap = [[0, src]]    # each value = [distance to vertex, vertex]
    visited = set()

    # run BFS
    while minHeap:
        w1, v1 = heapq.heappop(minHeap)
        if v1 in visited: continue

        for v2, w2 in adjacency_list[v1]:
            new_weight = shortest[v1] + w2
            if new_weight < shortest[v2]:
                shortest[v2] = new_weight
                heapq.heappush(minHeap, [new_weight, v2])
        visited.add(v1)

    for i in range(n):
        if i not in shortest:
            shortest[i] = -1
    return shortest



n = 5
edges = [[0, 1, 2], [0, 2, 4], [1, 2, 1], [1, 3, 7], [2, 4, 3], [3, 4, 1]]
src = 0
print(findShortestPath(n, edges, src))