class Solution:
    def floorSqrt(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2

            mid_sqr = mid * mid

            if mid_sqr == n:
                return mid
            elif mid_sqr > n:
                high = mid - 1
            else:
                low = mid + 1
        
        return high
            