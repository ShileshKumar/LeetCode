class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        result = 0
        start = 1
        end = x // 2

        while start <= end:
            mid = (start + end) // 2
            sqr = mid*mid
            
            if sqr == x:
                return mid
            elif sqr < x:
                start = mid + 1
                result = mid
            else:
                end = mid - 1

        return result