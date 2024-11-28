class Solution:
    def findKRotation(self, nums):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Pivot check
            if nums[mid] < nums[left] or nums[mid] > nums[right]:
                if nums[mid] < nums[left]:
                    return mid
                else:
                    return mid + 1
            
            elif nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1