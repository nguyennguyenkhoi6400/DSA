def bubble_sort(a, k):
    dem = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        dem+=1
    if dem == k:
        return True
    return False

a = [3, 2, 1]
k = 3
print(bubble_sort(a,k))