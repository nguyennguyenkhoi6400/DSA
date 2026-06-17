def insertion_b11(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and abs(a[j]) > abs(x):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    return a

a = [-3, 1, -2, 2]
print(insertion_b11(a))