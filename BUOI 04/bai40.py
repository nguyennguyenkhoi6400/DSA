def selection_b15(a, k):
    for i in range(k):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

a = [5, 3, 1, 4, 2]
k = 2
print(selection_b15(a, k))