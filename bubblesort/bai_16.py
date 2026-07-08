def bubble_sort_b16(a):
    dem = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                dem += 1
    return dem

a = [2, 3, 1]
print(bubble_sort_b16(a))