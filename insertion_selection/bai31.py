def selection_b6(a):
    dem = 0
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            dem += 1
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return dem

a = [5, 2, 4, 6, 1]
print("Số lần so sánh =", selection_b6(a))