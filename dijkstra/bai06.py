def dijkstra_st(adj, s, t):
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
        if u == t:
            return dist[t]
        visited[u] = True
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist[t]

adj = [
    [(1, 4), (2, 1)],      # 0
    [(3, 1)],              # 1
    [(1, 2), (3, 5), (4, 8)],  # 2
    [(4, 3), (5, 5)],      # 3
    [(5, 2)],              # 4
    []                     # 5
]
s = 0
t = 4
print(dijkstra_st(adj, s, t))