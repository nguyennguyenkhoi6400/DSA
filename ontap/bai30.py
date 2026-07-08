from collections import deque

def round_robin(process):

    queue = deque(process)

    while queue:

        job = queue.popleft()

        print(job)


round_robin(["P1", "P2", "P3"])