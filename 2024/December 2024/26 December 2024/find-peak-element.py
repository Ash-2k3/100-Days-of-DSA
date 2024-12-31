class Solution:
    def findPeakElement(self, arr):
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                return i

        if len(arr) >= 2:
            if arr[0] > arr[1]:
                return 0
            elif arr[-1] > arr[-2]:
                return len(arr) - 1