def selection_b17(a, k):
    for i in range(k):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a[k - 1]

a = [7, 2, 5, 1, 9]
k = 3
print(selection_b17(a, k))