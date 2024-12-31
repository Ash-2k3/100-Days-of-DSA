# Question link: https://takeuforward.org/plus/data-structures-and-algorithm/sorting/algorithms/selection-sort

class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            
            if min_index != i:
                nums[i], nums[min_index] = nums[min_index], nums[i]
        
        return nums
