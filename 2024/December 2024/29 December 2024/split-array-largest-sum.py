class Solution:
    def largestSubarraySumMinimized(self, a, k):
        min_sum = max(a)
        max_sum = sum(a)

        left = min_sum
        right = max_sum
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            sub_arr_is_possible = self.check_subarray_is_possible(
                a,
                k,
                mid
            )

            if sub_arr_is_possible:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1

        return ans
    
    @staticmethod
    def check_subarray_is_possible(arr, k, allowed_sum):
        sub_array_sum = 0
        splits = 1  # Start with one subarray

        for num in arr:
            if sub_array_sum + num > allowed_sum:
                splits += 1
                sub_array_sum = num  # Start a new subarray
                if splits > k:
                    return False
            else:
                sub_array_sum += num

        return True