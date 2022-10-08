class Solution:
    def myAtoi(self, s: str) -> int:
        import re
        patt = re.compile("^(\ *)([-+]?\d+)")
        matched = re.match(patt, s)
        num = 0
        if matched:
            str_num = matched[2]
            
            # for i, n in enumerate(matched[::-1]):
            #     if n:
            #         num += int(n) * 10 ** i
            
            num = int(str_num)
            max_ =  2**31 - 1
            min_ = (max_ + 1) * -1

            if num > max_:
                num = max_
                
            elif num < min_:
                num = min_
        
        return num
        
        
        