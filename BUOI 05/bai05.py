def dijkstra(adj, s):
    n = len(adj)
    dist = [float('inf')] * n
    visited = [False] * n
    dist[s] = 0

    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i]:
                if u == -1 or dist[i] < dist[u]:
                    u = i
        if u == -1:
            break
        visited[u] = True
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist

adj = [
    [(1,4), (2,3)],
    [(0,4), (3,2)],
    [(0,3), (3,3)],
    [(1,2), (2,3), (4,4)],
    [(3,4)]
]
dist = dijkstra(adj, 0)
for i in range(len(dist)):
    print(dist[i])