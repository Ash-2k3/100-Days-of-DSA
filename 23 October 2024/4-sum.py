class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        ans = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        curr_quad_sum = nums[i] + nums[j] + nums[k] + nums[l]
                        if curr_quad_sum == target:
                            quadruplet = [
                                nums[i],
                                nums[j],
                                nums[k],
                                nums[l]
                            ]
                            quadruplet.sort()
                            ans.append(quadruplet)
        return ans