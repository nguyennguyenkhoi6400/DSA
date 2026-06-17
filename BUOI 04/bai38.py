def selection_b13(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j][1] < a[min][1]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

a = [('An', 8), ('Ba', 5), ('Cuong', 7)]
print(selection_b13(a))