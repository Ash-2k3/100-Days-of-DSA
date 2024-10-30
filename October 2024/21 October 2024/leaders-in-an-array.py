class Solution:
    def leaders(self, nums):
        leaders = []
        max_right = float('-inf')
        
        for num in reversed(nums):
            if num > max_right:
                leaders.append(num)
                max_right = num
        
        return leaders[::-1]
