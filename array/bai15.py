class DanhSachMang:

    def __init__(self):

        self.du_lieu = []
        self.dem_sua = 0

    def them(self, x):

        self.du_lieu.append(x)
        self.dem_sua += 1

    def duyet(self):

        ban_dau = self.dem_sua

        for i in self.du_lieu:

            if ban_dau != self.dem_sua:

                raise Exception("Danh sach da bi sua")

            print(i)


ds = DanhSachMang()

ds.them(1)
ds.them(2)
ds.duyet()