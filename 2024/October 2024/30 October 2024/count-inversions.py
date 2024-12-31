class Solution:
    def __init__(self):
        self.count = 0

    def numberOfInversions(self, nums):
        self.findInversions(nums, 0, len(nums) - 1)
        return self.count
    
    def findInversions(self, nums, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.findInversions(nums, low, mid)
        self.findInversions(nums, mid + 1, high)
        self.mergeAndCount(nums, low, mid, high)
    
    def mergeAndCount(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        # Merge and count inversions
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                self.count += (mid - left + 1)  # Count all inversions
                right += 1

        # Copy remaining elements from the left half, if any
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Copy remaining elements from the right half, if any
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy the merged elements back to the original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
