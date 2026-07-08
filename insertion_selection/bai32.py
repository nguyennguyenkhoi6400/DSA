def selection_b7(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

a = ['d', 'a', 'c', 'b']
print(selection_b7(a))