class MangHaiChieu:

    def __init__(self):

        self.du_lieu = []

    def them_hang(self, hang):

        self.du_lieu.append(hang)

    def gan(self, i, j, gia_tri):

        self.du_lieu[i][j] = gia_tri

    def lay(self, i, j):

        return self.du_lieu[i][j]

    def hien_thi(self):

        for i in self.du_lieu:
            print(i)


m = MangHaiChieu()

m.them_hang([1, 2])
m.them_hang([3, 4])
m.gan(1, 0, 99)
m.hien_thi()