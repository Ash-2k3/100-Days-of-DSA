class Solution:
    def kthElement(self, a, b, k):
        itr = k
        ptr1, ptr2 = 0, 0
        curr_ans = 0
        while itr and ptr1 < len(a) and ptr2 < len(b):
            if a[ptr1] < b[ptr2]:
                curr_ans = a[ptr1]
                ptr1 += 1
                itr -= 1
            else:
                curr_ans = b[ptr2]
                ptr2 += 1
                itr -= 1

        if ptr1 >= len(a) and itr > 0:
            curr_ans = b[ptr2 - 1 + itr]
        elif ptr2 >= len(b) and itr > 0:
            curr_ans = a[ptr1 - 1 + itr]
   
        return curr_ans
                    