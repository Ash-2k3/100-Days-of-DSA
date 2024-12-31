class Solution:
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first_occ = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    first_occ = mid  # Potential first occurrence
                    right = mid - 1  # Search towards the left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return first_occ

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last_occ = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    last_occ = mid  # Potential last occurrence
                    left = mid + 1  # Search towards the right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return last_occ

        # Find the first and last occurrences
        first_occ = findFirst(nums, target)
        last_occ = findLast(nums, target)

        # If the target is not found, both will be -1
        return [first_occ, last_occ]
