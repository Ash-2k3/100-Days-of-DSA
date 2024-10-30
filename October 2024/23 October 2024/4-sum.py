class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        ans_set = set()

        for i in range(n):
            for j in range(i + 1, n):
                hash_set = set()
                for k in range(j + 1, n):
                    fourth_num = target - nums[i] - nums[j] - nums[k]
                    if fourth_num in hash_set:
                        quadruplet = [
                            nums[i],
                            nums[j],
                            nums[k],
                            fourth_num
                        ]
                        quadruplet.sort()
                        ans_set.add(tuple(quadruplet))
                    hash_set.add(nums[k])
        
        return list(ans_set)