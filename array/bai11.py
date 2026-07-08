class DanhSachMang:
    
    def dao(self, arr, left, right):
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            
            left += 1
            right -= 1
            
    def xoay_phai(self, arr, k):
        n = len(arr)
        k = k % n
        
        self.dao(arr, 0, n - 1)
        self.dao(arr, 0, k - 1)
        self.dao(arr, k, n - 1)
        
        return arr
    
ds = DanhSachMang()
arr = [1, 2, 3, 4, 5]

print(ds.xoay_phai(arr, 2))
    