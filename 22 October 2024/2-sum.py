class Solution:
    def twoSum(self, nums, target):
        ans = []
        map_val_to_index = {}

        for i, val in enumerate(nums):
            target_val = target - val
            if target_val in map_val_to_index:
                ans.append(map_val_to_index[target_val])
                ans.append(i)
                return ans

            map_val_to_index[val] = i
        
        return ans