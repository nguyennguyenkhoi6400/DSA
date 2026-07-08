def tim_kiem(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        center = (left + right) // 2
        
        if arr[center] == x:
            return center
        
        if arr[center] < x:
            left = center + 1
            
        else:
            right = center - 1
            
    return - 1

print(tim_kiem([1, 3, 5, 7, 9], 7))
            