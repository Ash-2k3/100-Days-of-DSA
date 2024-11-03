class Solution:
    def maxProduct(self, nums):
        suffix_arr = [1 for _ in range(len(nums))]
        preffix_arr = []

        # Calculate the prefix
        for i, num in enumerate(nums):
            if i == 0:
                preffix_arr.append(1)
                continue

            curr_product = nums[i - 1] * preffix_arr[i - 1]
            if preffix_arr[i - 1] == 0:
                preffix_arr.append(nums[i - 1])
            else:
                preffix_arr.append(curr_product)

        # Calculate the suffix
        for i in range(len(nums) - 2, -1, -1):
            curr_product = suffix_arr[i + 1] * nums[i + 1]
            if suffix_arr[i + 1] == 0:
                suffix_arr[i] = nums[i + 1]
            else:
                suffix_arr[i] = curr_product

        ans = float('-inf')
        # Calculating the Result
        for i in range(len(nums)):
            ans = max(ans, suffix_arr[i]*nums[i], preffix_arr[i]*nums[i], nums[i])

        return ans
