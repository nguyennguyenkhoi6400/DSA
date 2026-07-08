def bubble_sort_b10(a):
    tong = 0
    for i in range(len(a)):
        tam = False
        tong += 1
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                tam = True
        if not tam:
            break
    return tong

a = [2, 1, 3, 4]
print(bubble_sort_b10(a))