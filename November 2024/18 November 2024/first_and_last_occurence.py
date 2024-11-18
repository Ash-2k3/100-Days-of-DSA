class Solution:
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left<= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                first_occ, last_occ = mid, mid
                pointer = mid
                while pointer >= 0 and nums[pointer] == target:
                    first_occ = pointer
                    pointer -= 1

                pointer = mid

                while pointer < len(nums) and nums[pointer] == target:
                    last_occ = pointer
                    pointer += 1
                
                return [first_occ, last_occ]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]
