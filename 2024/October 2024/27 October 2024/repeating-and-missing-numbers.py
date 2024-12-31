class Solution:
    def findMissingRepeatingNumbers(self, nums):
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        ans = [0, 0]
        for i in range(1, len(nums) + 1):
            if i not in freq_map:
                ans[1] = i
            elif freq_map[i] > 1:
                ans[0] = i
        
        return ans