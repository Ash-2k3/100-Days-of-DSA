# Question link: https://takeuforward.org/plus/data-structures-and-algorithm/sorting/algorithms/bubble-sort/submissions

class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            swapped = False
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums
