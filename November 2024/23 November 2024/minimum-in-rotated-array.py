class Solution:
    def findMin(self, arr):
        left = 0
        right = len(arr) - 1
        min_ele = float('inf')

        while left <= right:
            mid = (left + right) // 2

            min_ele = min(arr[mid], min_ele)

            # If left part is sorted
            if arr[mid] >= arr[left]:
                min_ele = min(arr[left], min_ele)

                left = mid + 1
            
            # If the right part is sorted
            else:
                right = mid - 1
        
        return min_ele