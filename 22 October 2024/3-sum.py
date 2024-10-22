class Solution:
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n -1 ):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        if sorted(triplet) not in ans:
                            ans.append(sorted(triplet))
        return ans