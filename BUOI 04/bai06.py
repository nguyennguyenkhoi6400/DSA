def insertion_b6(a):
    dem = 0
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0:
            dem += 1
            if a[j] > x:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = x
    return dem

a = [1, 2, 3]
print("Số lần so sánh =", insertion_b6(a))