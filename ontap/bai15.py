import heapq

def dijkstra(graph, start):

    distance = {node: float("inf") for node in graph}
    distance[start] = 0

    heap = [(0, start)]

    while heap:

        cost, node = heapq.heappop(heap)

        if cost > distance[node]:
            continue

        for next_node, weight in graph[node]:

            new_cost = cost + weight

            if new_cost < distance[next_node]:

                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return distance


graph = {
    "A":[("B",4),("C",2)],
    "B":[("D",5)],
    "C":[("B",1),("D",8)],
    "D":[]
}

print(dijkstra(graph,"A"))