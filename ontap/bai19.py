from collections import deque

grid = [
    [0,0,0],
    [1,1,0],
    [0,0,0]
]

queue = deque([(0,0)])
visited = {(0,0)}

move = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:

    row, col = queue.popleft()

    print(row, col)

    for dr, dc in move:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            if grid[new_row][new_col] == 0 and (new_row,new_col) not in visited:

                visited.add((new_row,new_col))
                queue.append((new_row,new_col))