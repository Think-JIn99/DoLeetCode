class Solution:
    def isPalindrome(self, x: int) -> bool:
        r_num = 0
        num = x
        if x < 0: return False
        while x:
            r_num = 10 * r_num + x % 10
            x = x // 10
        return r_num == num
                
            
        