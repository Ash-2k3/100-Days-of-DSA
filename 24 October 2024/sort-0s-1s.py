class Solution:
    def sortZeroOneTwo(self, nums):
        ans = [-1 for _ in range(len(nums))]
        n = len(ans)
        left_ptr = 0
        right_ptr = n - 1

        for num in nums:
            if num == 0:
                ans[left_ptr] = 0
                left_ptr += 1
            elif num == 2:
                ans[right_ptr] = 2
                right_ptr -= 1
        
        while left_ptr <= right_ptr:
            ans[left_ptr] = 1
            left_ptr += 1
        
        for i in range(n):
            nums[i] = ans[i]

        return ans