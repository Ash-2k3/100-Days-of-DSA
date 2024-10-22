class Solution:
    def twoSum(self, nums, target):
        map_val_to_index = {}

        for i, val in enumerate(nums):
            target_val = target - val
            if target_val in map_val_to_index:
                return [map_val_to_index[target_val], i]

            map_val_to_index[val] = i

        return []