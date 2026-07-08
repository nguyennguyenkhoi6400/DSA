def phan_tu_cuoi_cung(a):
    max = a[0]
    for i in range(len(a)):
        if max <= a[i]:
            max = a[i]
    return max

a = [4, 2, 7, 1, 3]
print(phan_tu_cuoi_cung(a))