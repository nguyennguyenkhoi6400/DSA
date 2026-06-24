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
    [(1, 4), (2, 1)],
    [(3, 1)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3), (5, 5)],
    [(5, 2)],
    []
]

s = 0
D = 3
dist = dijkstra(adj, s)
print("Khoảng cách từ đỉnh", s)
for i in range(len(dist)):
    print("Đỉnh", i, "=", dist[i])
dem = 0
for i in range(len(dist)):
    if dist[i] <= D:
        dem += 1
print("Số đỉnh có khoảng cách <=", D, "là:", dem)
print("Các đỉnh thỏa mãn:")
for i in range(len(dist)):
    if dist[i] <= D:
        print(i, end=" ")