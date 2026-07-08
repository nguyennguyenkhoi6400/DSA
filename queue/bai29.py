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
    
class BoDemSuKien:
    def __init__(self, t_giay):
        self.q = Queue()
        self.t = t_giay 
        
    def ghi_nhan_hit(self, thoi_gian_hien_tai):
        self.q.enqueue(thoi_gian_hien_tai)
        while not self.q.isEmpty() and self.q.front() < thoi_gian_hien_tai - self.t:
            self.q.dequeue()
            
    def lay_so_luong_hit(self, thoi_gian_hien_tai):
        while not self.q.isEmpty() and self.q.front() < thoi_gian_hien_tai - self.t:
            self.q.dequeue()
        return len(self.q.items)

counter = BoDemSuKien(300)
counter.ghi_nhan_hit(10)
counter.ghi_nhan_hit(50)
counter.ghi_nhan_hit(320)
print("Số hit hợp lệ còn lại:", len(counter.q.items))