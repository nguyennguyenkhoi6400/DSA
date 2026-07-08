class DanhSachMang:

    def tron(self, a, b):
        ket_qua = []

        i = 0
        j = 0

        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                ket_qua.append(a[i])
                i += 1
            
            else:
                ket_qua.append(b[j])
                j += 1

        while i < len(a):
            ket_qua.append(a[i])
            i += 1

        while j < len(b):
            ket_qua.append(b[j])
            j += 1

        return ket_qua


ds = DanhSachMang()

a = [1, 3, 5]
b = [2, 4]

print(ds.tron(a, b))