class Solution:
    def findMissingRepeatingNumbers(self, nums):
        nums.sort()
        ans = [0, 0]
        for i in range(1, len(nums)):
            # Condition to check repeating number.
            if nums[i] - nums[i -1] == 0:
                ans[0] = nums[i]
            elif nums[i] - nums[i - 1] > 1:
                ans[1] = nums[i-1] + 1

        # print(ans)
        if ans[1] == 0:
            if nums[0] == 2:
                ans[1] = 1
            elif nums[-1] == len(nums) - 1:
                ans[1] = len(nums)
        
        return ans

            