class Solution:
    def mergeSort(self, nums):
        print('I am here')
        self.sort(nums, 0, len(nums) - 1)

        return nums
    
    def sort(self, arr, low, high):
        print(low, high)
        if low >= high:
            return
 
        mid = int((low + high)/2)
        self.sort(arr, low, mid)
        self.sort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)
   
    def merge(self, arr, low, mid, high):
        temp = []

        left = low
        right = mid + 1

        while (left <= mid and right <= high):
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        
        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1
        
        # Copy the merged elements back to the original array
        for i in range(len(temp)):
            arr[low + i] = temp[i]
