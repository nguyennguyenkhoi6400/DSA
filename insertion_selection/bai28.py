def selection_b3(a):
    for i in range(len(a) - 1):
        max = i
        for j in range(i + 1, len(a)):
            if a[j] > a[max]:
                max = j
        a[i], a[max] = a[max], a[i]
    return a

a = [5, 2, 4, 6, 1]
print(selection_b3(a))