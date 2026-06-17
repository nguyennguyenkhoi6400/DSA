def selection_b8(a, i):
    min = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min]:
            min = j
    return min

a = [9, 3, 7, 1, 5]
i = 1
print(selection_b8(a, i))