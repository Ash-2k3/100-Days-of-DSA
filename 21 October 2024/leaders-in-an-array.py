class Solution:
    def leaders(self, nums):
        n = len(nums)
        maxEleInRight = float('-inf')
        leaders_list = []
        for i in range(n - 1, -1, -1):
            if nums[i] > maxEleInRight:
                maxEleInRight = nums[i]
                leaders_list.append(maxEleInRight)

        leaders_list.reverse()
        return leaders_list