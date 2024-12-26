class Solution:
    def findPages(self, nums, m):
        if m > len(nums):
            return -1
        students = m
        books = len(nums)
        upper_limit = sum(nums)
        lower_limit = max(nums)
        curr_limit = lower_limit
        curr_pages = 0
        i = 0

        while curr_limit <= upper_limit:
            while m >= 1:
                if i < books and curr_pages + nums[i] <= curr_limit:
                    curr_pages += nums[i]
                    i += 1
                else:
                    m -= 1
                    curr_pages = 0
                if i >= books:
                    return curr_limit
            curr_limit += 1
            m = students
            i = 0
            curr_pages = 0
        
        return -1
