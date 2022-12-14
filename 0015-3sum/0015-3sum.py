class Solution:                
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, first_num in enumerate(nums[:-2]):
            left = i + 1
            right = len(nums) - 1
            
            if i > 0 and nums[i] == nums[i-1]: continue
            
            while left < right:
                sum_ = first_num + nums[left] + nums[right]
                if sum_ > 0:
                    right -= 1
                  
                elif sum_ < 0:
                    left += 1
                   
                elif sum_ == 0:
                    res.append([first_num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -=1
        
        return res
                
            
           
        
        
            
        return res
        