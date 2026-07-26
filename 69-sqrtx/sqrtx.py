class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        if x == 0:
            return 0
            
        low = 1
        high = x // 2
        ans = 0

        while low<=high:
            mid = low + (high - low) // 2

            sq = mid * mid

            print(low, high, mid, sq)

            if sq == x:
                return mid
            elif sq < x:
                ans = mid
                low = mid + 1
            elif sq > x:
                high = mid - 1
        
        return ans