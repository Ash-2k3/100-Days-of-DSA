class Solution:
    def searchMatrix(self, mat, target):
        left = 0
        right = len(mat) - 1
        row_size = len(mat[0])

        while left <= right:
            mid = (left + right) // 2

            if mat[mid][0] <= target <= mat[mid][-1]:
                result = self.search_for_target(mat[mid], target)
                return result
            else:
                if mat[mid][0] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return False
    
    def search_for_target(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) //2

            if target == arr[mid]:
                return True
            elif target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False
     