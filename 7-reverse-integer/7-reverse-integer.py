class Solution:
    def reverse(self, x: int) -> int:
        sign = (x > 0) - (x < 0)            
        reveresed_ = sign * int(str(x * sign)[::-1])
        if reveresed_ > 2147483647 or reveresed_ < -2147483648: 
            return 0
        
        return reveresed_