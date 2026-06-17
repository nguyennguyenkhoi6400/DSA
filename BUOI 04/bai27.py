def selection_b2(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

a = [5, 2, 4, 6, 1, 3]
print(selection_b2(a))