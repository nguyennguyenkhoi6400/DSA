def one_pass_bubble_sort(arr):
    n = len(arr)
    # Chỉ thực hiện duy nhất 1 lượt duyệt từ trái sang phải
    for j in range(0, n - 1):
        if arr[j] > arr[j + 1]:
            # Hoán đổi nếu sai thứ tự tăng dần
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Chạy thử nghiệm
a = [5, 1, 4, 2, 8]
print("Bài 1:", one_pass_bubble_sort(a))
# Kết quả mong muốn: [1, 4, 2, 5, 8]