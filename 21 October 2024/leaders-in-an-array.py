class Solution:
    def leaders(self, nums):
        leaders_list = []

        # A Flag to check if there's any leader in the current window of elements.
        leader_found = False
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] <= nums[j]:
                    leader_found = False
                    break
                leader_found = True
            if leader_found:
                leaders_list.append(nums[i])  
            leader_found = False

        leaders_list.append(nums[-1])
        return leaders_list
