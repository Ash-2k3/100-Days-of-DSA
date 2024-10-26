class Solution:
    def majorityElement(self, nums):
        max_ele = nums[0]
        max_count = 1

        for i in range(1, len(nums)):
            if nums[i] == max_ele:
                max_count += 1
            else:
                max_count -= 1

                if max_count < 0:
                    max_ele = nums[i]
                    max_count = 1
        
        return max_ele