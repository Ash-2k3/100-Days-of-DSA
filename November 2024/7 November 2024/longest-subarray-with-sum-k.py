class Solution:
    def longestSubarray(self, nums, k):
        prefix_sum_map = {}

        prefix_sum = 0
        max_streak = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            prefix_sum_map[prefix_sum] = i

            if prefix_sum - k in prefix_sum_map:
                max_streak = max(i - prefix_sum_map[prefix_sum - k], max_streak)
            
            if prefix_sum == k:
                max_streak = max(i + 1, max_streak)
        
        return max_streak
