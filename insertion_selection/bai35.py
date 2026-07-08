def selection_b10(a):
    dem = 0
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        if min != i:
            a[i], a[min] = a[min], a[i]
            dem += 1
    return dem

a = [1, 2, 3]
print("Số lần hoán đổi =", selection_b10(a))