class Solution:
    def heapify(self,arr, n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        
        if l<n and arr[largest] < arr[l]:
            largest = l
        
        if r<n and arr[largest] < arr[r]:
            largest = r
            
        if largest != i:
            arr[largest], arr[i] = arr[i],arr[largest]
            self.heapify(arr,n,largest)
    
    def buildHeap(self,arr,n):
        for i in range( (n//2)-1, -1, -1 ):
            self.heapify(arr, n, i)

    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        for i in range(n-1,0,-1):
            arr[i],arr[0] = arr[0],arr[i]
            self.heapify(arr, i, 0)


N = 5
arr = [4,1,3,9,7]

obj = Solution()

print("original: ", arr)
obj.HeapSort(arr,N)

print("sorted: ", arr)