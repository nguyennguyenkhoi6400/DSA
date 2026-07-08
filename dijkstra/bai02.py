def dijkstra_tay(adj, s):
    n = len(adj)
    dist = [float('inf')] * n
    visited = [False] * n
    dist[s] = 0

    for buoc in range(n):
        u = -1
        for i in range(n):
            if not visited[i]:
                if u == -1 or dist[i] < dist[u]:
                    u = i
        visited[u] = True
        print("Bước", buoc + 1, "- Chốt đỉnh", u)
        print("dist =", dist)
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist

adj = [
    [(1,4),(2,1)],
    [(3,1)],
    [(1,2),(3,5),(4,8)],
    [(4,3),(5,5)],
    [(5,2)],
    []
]
dijkstra_tay(adj, 0)