class Solution:
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        triplet_set = set()
        nums.sort()
        for i in range(n - 2):
            target_val = -1*nums[i]
            left_ptr = i + 1
            right_ptr = n - 1
            while left_ptr < right_ptr:
                if nums[left_ptr] + nums[right_ptr] == target_val:
                    triplet = [nums[left_ptr],nums[right_ptr], nums[i] ]
                    if tuple(triplet) in triplet_set:
                        left_ptr += 1
                        right_ptr -= 1
                    else:
                        triplet_set.add(tuple(triplet))
                        ans.append(triplet)
                elif nums[left_ptr] + nums[right_ptr] > target_val:
                    right_ptr -= 1
                else:
                    left_ptr += 1
        return ans