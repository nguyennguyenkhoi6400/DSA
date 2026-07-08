def bubble_sort_b5(a):
    dem = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            dem += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return dem

a = [1, 2, 3]
print(bubble_sort_b5(a))