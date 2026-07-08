def insertion_b13(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j][0] > x[0]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    return a

a = [(2, 'a'), (1, 'b'), (2, 'c')]
print(insertion_b13(a))