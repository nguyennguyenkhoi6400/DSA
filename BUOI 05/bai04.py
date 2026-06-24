def dijkstra(adj, s):
    n = len(adj)
    dist = [float('inf')] * n
    visited = [False] * n
    dist[s] = 0

    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        if u == -1:
            break
        visited[u] = True
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist

adj = [
    [(1,4), (2,1)],
    [(3,1)],
    [(1,2), (3,5), (4,8)],
    [(4,3), (5,5)],
    [(5,2)],
    []
]

dist = dijkstra(adj, 0)
for i in range(len(dist)):
    if dist[i] == float('inf'):
        print(f"Đỉnh {i}: -1")
    else:
        print(f"Đỉnh {i}: {dist[i]}")