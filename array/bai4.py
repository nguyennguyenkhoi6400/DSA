class DanhSachMang:

    def __init__(self):
        self.du_lieu = []

    def tim_vi_tri(self, gia_tri):

        for i in range(len(self.du_lieu)):
            if self.du_lieu[i] == gia_tri:
                return i

        return -1


ds = DanhSachMang()

ds.du_lieu = [5, 3, 7]

print(ds.tim_vi_tri(7))