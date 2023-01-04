from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cmax = nums[0]
        cmin = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            values = (num, cmax*num, cmin*num)
            
            cmax = max(cmax,*values)
            cmin = min(cmin,*values)
            
    
        return cmax


s = Solution()
print(s.maxProduct([2, -3, 1, 0, -5]))