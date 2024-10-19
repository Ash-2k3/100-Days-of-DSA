# Question 1 link: https://takeuforward.org/plus/data-structures-and-algorithm/sorting/algorithms/selection-sort

class Solution:
    def selectionSort(self, nums):
        write_index = 0
        read_index = 0
        while write_index < len(nums):
            min_ele = float('inf')
            min_index = -1
            for i in range(read_index, len(nums)):
                if min_ele > nums[i]:
                    min_ele = nums[i]
                    min_index = i
            
            nums[write_index], nums[min_index] = nums[min_index], nums[write_index]

            write_index += 1
            read_index += 1
        
        return nums
