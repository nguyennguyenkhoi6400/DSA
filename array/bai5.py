class DanhSachMang:

    def __init__(self):
        self.du_lieu = []

    def duyet(self):

        for i in self.du_lieu:
            print(i)

    def dem_chan(self):

        dem = 0

        for i in self.du_lieu:
            if i % 2 == 0:
                dem += 1

        return dem


ds = DanhSachMang()

ds.du_lieu = [1, 2, 3, 4]
ds.duyet()

print("Số chẵn:", ds.dem_chan())