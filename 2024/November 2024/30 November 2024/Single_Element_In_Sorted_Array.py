class Solution:
    """ Function to find the single non 
        duplicate element in a sorted array """
    def singleNonDuplicate(self, nums):
        n = len(nums) # Size of the array.

        # Edge cases:
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        low, high = 1, n - 2
        while low <= high:
            mid = (low + high) // 2

            # If nums[mid] is the single element:
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]

            # We are in the left part:
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                # Eliminate the left half:
                low = mid + 1
            # We are in the right part:
            else:
                # Eliminate the right half:
                high = mid - 1

        # Dummy return statement:
        return -1

