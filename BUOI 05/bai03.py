def dijkstra(adj, s):
    n = len(adj)
    dist = [float('inf')] * n
    visited = [False] * n
    dist[s] = 0
    for k in range(n):
        u = -1
        # tìm đỉnh chưa xét có khoảng cách nhỏ nhất
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        visited[u] = True
        # duyệt các đỉnh kề của u
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist

adj = [
    [(1,4), (2,1)],
    [(3,1)],
    [(1,2), (3,5), (4,8)],
    [(4,3), (5,6)],
    [(5,2)],
    []          # đỉnh 5
]
s=0
print(dijkstra(adj,s))