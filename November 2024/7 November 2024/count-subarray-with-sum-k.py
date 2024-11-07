class Solution:
    def subarraySum(self, nums, k):
        prefix_sum_map = {0: 1}  # Initialize with 0 prefix sum for subarrays starting from the beginning.
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            # Check if prefix_sum - k exists in the map
            if prefix_sum - k in prefix_sum_map:
                count += prefix_sum_map[prefix_sum - k]

            # Update the map with the current prefix_sum
            prefix_sum_map[prefix_sum] = prefix_sum_map.get(prefix_sum, 0) + 1

        return count
