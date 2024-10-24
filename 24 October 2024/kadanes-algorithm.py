class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]

        for i in range(len(nums)):
            subarray_sum = 0
            for j in range(i, len(nums)):
                subarray_sum += nums[j]
                max_sum = max(max_sum, subarray_sum)

        return max_sum