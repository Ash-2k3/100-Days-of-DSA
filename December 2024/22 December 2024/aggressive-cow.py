class Solution:
    def aggressiveCows(self, nums, k):
        # sort the array
        nums.sort()
        searchSpace = nums[-1] - nums[0]
        ans = 0
        for i in range(1, searchSpace + 1):
            if self.canWePlace(i, nums, k):
                ans = i
                continue
            else:
                break
        return ans

    @staticmethod
    def canWePlace(dis, nums, k):
        last_placed_index = 0
        cows_to_place = k - 1
        for i in range(1, len(nums)):
            if nums[i] - nums[last_placed_index] >= dis:
                cows_to_place -= 1
                last_placed_index = i
            if cows_to_place == 0:
                return True
        return False