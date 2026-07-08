class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, x):
        self.items.append(x)
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Underflow")
        return self.items.pop(0) 
    
    def front(self):
        if self.isEmpty():
            raise IndexError("Hàng đợi rỗng")
        return self.items[0] 
    
    def isEmpty(self):
        return len(self.items) == 0
    
def btoan_josephus(n, k):
    q = Queue()
    for i in range(1, n + 1):
        q.enqueue(i)
        
    while len(q.items) > 1:
        for dem in range(k - 1):
            nguoi_qua_luot = q.dequeue()
            q.enqueue(nguoi_qua_luot)
        nguoi_bi_loai = q.dequeue()
    return q.dequeue()

print("Người sống sót cuối cùng của (n=5, k=2):", btoan_josephus(5, 2))