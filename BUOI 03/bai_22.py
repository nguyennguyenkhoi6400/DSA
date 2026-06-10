def bubble_sort_b22(a):
    dem = 0
    for i in range(len(a)):
        tam = False
        dem += 1
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                tam = True
        if not tam:
            break
    return dem

a = [2, 1, 4, 3, 6, 5]
print("Số lượt duyệt thực tế:", bubble_sort_b22(a))