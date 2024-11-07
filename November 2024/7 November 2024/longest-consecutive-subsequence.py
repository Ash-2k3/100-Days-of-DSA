class Solution:
    def longestConsecutive(self, nums):
        nums_set = sorted(set(nums))

        cnt = 0
        max_count = 0
        for i in range(len(nums_set) - 1):
            if nums_set[i + 1] == nums_set[i] + 1:
                cnt += 1
                max_count = max(cnt, max_count)
            else:
                cnt = 0
        
        return max_count + 1  


# Line 4: Suggest renaming 'cnt' to 'current_streak' for clarity
# Line 5: Consider renaming 'max_count' to 'longest_streak' to be more descriptive
# Line 8-11: Suggest adding a comment explaining the logic of checking and updating consecutive numbers
