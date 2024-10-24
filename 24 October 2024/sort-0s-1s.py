class Solution:
    def sortZeroOneTwo(self, nums):
        n = len(nums)
        zero_ptr = 0
        two_ptr = n - 1

        i = 0
        while(i <= two_ptr):
            if nums[i] == 0:
                nums[i], nums[zero_ptr] = nums[zero_ptr], nums[i]
                zero_ptr += 1
                i += 1

            elif nums[i] == 2:
                nums[i], nums[two_ptr] = nums[two_ptr], nums[i]
                two_ptr -= 1
            else:
                i += 1
        
        return nums