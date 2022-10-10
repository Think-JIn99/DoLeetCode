class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        right = len(num) // 2 + 1 if len(num) % 2 else len(num) // 2
        return num[:len(num) // 2] == num[right:][::-1]
                
            
        