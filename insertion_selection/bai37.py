def selection_b12(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        x = a[min]
        while min > i:
            a[min] = a[min - 1]
            min -= 1
        a[i] = x
    return a

a = [(2, 'a'), (2, 'b'), (1, 'c')]
print(selection_b12(a))