def bubble_sort_b23(a):
    comparisons = 0
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            comparisons += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
    return {"comparisons": comparisons, "swaps": swaps}

a = [140, 25, 15, 52, 10]
perf_metrics = bubble_sort_b23(a)
print("Số lần so sánh:", perf_metrics["comparisons"])
print("Số lần hoán đổi (swap):", perf_metrics["swaps"])