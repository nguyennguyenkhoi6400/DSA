def insertion_b1(a, x):
    a.append(x)
    i = len(a) - 2
    while i >= 0 and a[i] > x:
        a[i + 1] = a[i]
        i -= 1
    a[i + 1] = x
    return a

a = [1, 3, 5, 7]
x = 4
print(insertion_b1(a, x))