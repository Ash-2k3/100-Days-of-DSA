class Solution:
    def search(self, nums, k):
        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = (left + right) // 2

            if nums[mid] == k:
                return mid
            elif nums[mid] > nums[left]:
                # Left Array is sorted
                if nums[mid] > k and nums[left] <= k:
                    # Element is indeed in left part of the array.
                    right = mid - 1
                else:
                    # Although array is sorted, the element is not in left portion.
                    # Search in right portion
                    left = mid + 1
            else:
                # Right part is sorted.
                if nums[mid] < k and nums[right] >= k:
                    # Element is indeed in the right part.
                    left = mid + 1
                else:
                    # Although the right part is sorted the element is not here.
                    right = mid - 1


        return -1