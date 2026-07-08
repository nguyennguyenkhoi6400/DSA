def insertion_b14(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and (a[j][1] < x[1] or (a[j][1] == x[1] and a[j][0] > x[0])):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    return a

a = [('An', 8), ('Ba', 9), ('Cu', 8)]
print(insertion_b14(a))