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

def lap_lich_round_robin(cac_tien_trinh, quantum):
    q = Queue()
    for p in cac_tien_trinh:
        q.enqueue(p)
    thoi_gian_he_thong = 0
    print("Thứ tự xử lý tiến trình:")
    while not q.isEmpty():
        p_hien_tai = q.dequeue()
        ten = p_hien_tai[0]
        tg_con_lai = p_hien_tai[1]
        if tg_con_lai <= quantum:
            thoi_gian_he_thong += tg_con_lai
            print(f" -> Tiến trình {ten} HOÀN THÀNH tại thời điểm: {thoi_gian_he_thong}")
        else:
            thoi_gian_he_thong += quantum
            tg_con_lai -= quantum
            q.enqueue([ten, tg_con_lai])

danh_sach_p = [["A", 5], ["B", 2]] 
lap_lich_round_robin(danh_sach_p, quantum=2)