from collections import deque

def bfs(graph, start):

    queue = deque([start])
    visited = {start}

    while queue:

        node = queue.popleft()

        print(node, end=" ")

        for next_node in graph[node]:

            if next_node not in visited:

                visited.add(next_node)
                queue.append(next_node)


graph = {
    "A":["B","C"],
    "B":["D"],
    "C":["E"],
    "D":[],
    "E":[]
}

bfs(graph, "A")