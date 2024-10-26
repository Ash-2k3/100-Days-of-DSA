class Solution:
    def majorityElement(self, nums):
        freq_map = {}

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        max_count = 0
        max_ele = 0

        for key, val in freq_map.items():
            if max_count < val:
                max_count = val
                max_ele = key
            
        return max_ele