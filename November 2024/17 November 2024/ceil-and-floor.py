class Solution:
    def getFloorAndCeil(self, nums, x):
        def getFloor():
            left = 0 
            right = len(nums) - 1
            floor_value = float('-inf')
            while left <= right:
                middle = (left + right) // 2

                if nums[middle] > x:
                    right = middle - 1
                else:
                    left = middle + 1
                    floor_value = max(floor_value, nums[middle])
            
            return floor_value if floor_value != float('-inf') else -1
        
        def getCeil():
            left = 0 
            right = len(nums) - 1
            ceil_value = float('inf')
            while left <= right:
                middle = (left + right) // 2

                if nums[middle] >= x:
                    right = middle - 1
                    ceil_value = min(ceil_value, nums[middle])
                else:
                    left = middle + 1
            
            return ceil_value if ceil_value != float('inf') else -1

        ceil = getCeil()
        floor = getFloor()
        return [floor, ceil]
