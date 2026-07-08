def bubble_sort(arr):
    dem  = 0
    
    for i in range(len(arr) - 1):
        
        for j in range(len(arr) - 1 - i):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                dem += 1
                
    print(arr)
    print("So lan doi: ", dem)
    
bubble_sort([2, 3, 1])
            