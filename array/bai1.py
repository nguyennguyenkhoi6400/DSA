class DanhSachMang:

    def __init__(self):
        self.du_lieu = []

    def them(self, gia_tri):
        self.du_lieu.append(gia_tri)

    def lay(self, vi_tri):
        return self.du_lieu[vi_tri]

    def gan(self, vi_tri, gia_tri_moi):
        self.du_lieu[vi_tri] = gia_tri_moi

    def kich_thuoc(self):
        return len(self.du_lieu)

    def hien_thi(self):
        print(self.du_lieu)


ds = DanhSachMang()

ds.them(1)
ds.them(2)
ds.them(3)

print("Danh sách:")
ds.hien_thi()

print("Lấy vị trí 1:", ds.lay(1))

ds.gan(1, 99)

print("Sau khi sửa:")
ds.hien_thi()

print("Kích thước:", ds.kich_thuoc())