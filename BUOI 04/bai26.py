def selection_b1(a):
    min = 0
    for i in range(1, len(a)):
        if a[i] < a[min]:
            min = i
    a[0], a[min] = a[min], a[0]
    return a

a = [4, 2, 7, 1, 3]
print(selection_b1(a))