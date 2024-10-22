class Solution:
    def twoSum(self, nums, target):
        ans = []
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans

        return ans