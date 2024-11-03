class Solution:
    def merge(self, nums1, m, nums2, n):
        m_ptr = m - 1
        n_ptr = 0

        while m_ptr >= 0 and n_ptr < n:
            if nums1[m_ptr] > nums2[n_ptr]:
                nums1[m_ptr], nums2[n_ptr] = nums2[n_ptr], nums1[m_ptr]

            m_ptr -= 1
            n_ptr += 1

        nums1[:m] = sorted(nums1[:m])
        nums2.sort()
        for num in nums2:
            nums1[m] = num
            m += 1
