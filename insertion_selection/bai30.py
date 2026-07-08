def selection_b5(a):
    dem = 0
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
        dem += 1
    return dem

a = [3, 2, 1]
print("Số lần hoán đổi =", selection_b5(a))