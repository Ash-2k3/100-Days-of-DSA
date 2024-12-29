class Solution:
    def median(self, arr1, arr2):
        new_arr = []

        n = len(arr1) + len(arr2)
        k = n // 2
        ptr1, ptr2 = 0, 0
        while k + 1 and ptr1 < len(arr1) and ptr2 < len(arr2):
            if arr1[ptr1] < arr2[ptr2]:
                new_arr.append(arr1[ptr1])
                ptr1 += 1
            else:
                new_arr.append(arr2[ptr2])
                ptr2 += 1
            k -= 1

        while k + 1 and ptr1 < len(arr1):
            new_arr.append(arr1[ptr1])
            ptr1 += 1
            k -= 1

        while k + 1 and ptr2 < len(arr2):
            new_arr.append(arr2[ptr2])
            ptr2 += 1
            k -= 1

        median = 0
        if n % 2 == 0:
            median = (new_arr[-1] + new_arr[-2]) / 2
        else:
            median = (new_arr[-1])
        
        return median