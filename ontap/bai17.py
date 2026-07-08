import heapq

heap = []

heapq.heappush(heap,(4,"B"))
heapq.heappush(heap,(2,"C"))
heapq.heappush(heap,(1,"A"))

while heap:

    print(heapq.heappop(heap))