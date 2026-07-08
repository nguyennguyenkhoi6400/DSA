def insertion_b17(a):
    dem = 0
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            dem += 1
            j -= 1
        a[j + 1] = x
    return dem

a = [1, 2, 4, 3, 5]
print("Số lần dịch chuyển =", insertion_b17(a))