class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            current_num = nums[i]

            # When multiplying by a negative number, swap max and min
            if current_num < 0:
                max_so_far, min_so_far = min_so_far, max_so_far

            # Update max and min products at this position
            max_so_far = max(current_num, max_so_far * current_num)
            min_so_far = min(current_num, min_so_far * current_num)

            # Update result with the largest product found so far
            result = max(result, max_so_far)

        return result
