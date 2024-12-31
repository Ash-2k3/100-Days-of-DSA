class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)

        max_count = 1

        for num in nums_set: 
            if num - 1 in nums_set:
                continue
            else:
                cnt = 1
                while num + 1 in nums_set:
                    cnt += 1
                    num += 1
    
                max_count = max(cnt, max_count)

        return max_count