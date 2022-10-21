class Solution:
    def binary_search(self, num, nums, left):
        # left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < num:
                left = mid + 1
            elif nums[mid] > num:
                right = mid - 1
            elif nums[mid] == num: return mid
        
        return -1
                
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        min_ = nums[-1]
        two_sum_min = nums[-2] + nums[-1]
        res = []
        f_visited = set()
        for i, first_num in enumerate(nums):
            
            if first_num > two_sum_min:
                break
            
            if first_num in f_visited: continue
            s_visited = set()
            
            for j, second_num in enumerate(nums[i+1:], start=i+1):
                if second_num in s_visited: continue
                
                two_sum = first_num + second_num
                if two_sum > min_: break
                
                idx = self.binary_search(-two_sum, nums, j + 1)
                
                if idx > j:
                    res.append([first_num, second_num, nums[idx]])
                
                s_visited.add(second_num)
            
            f_visited.add(first_num)
            
        return res
        