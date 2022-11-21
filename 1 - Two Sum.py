from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_dict = dict( (num,i) for i,num in enumerate(nums))

    for i,num in enumerate(nums):

        remainder = target - num
        
        if remainder in nums_dict.keys() and nums_dict[remainder] != i:
            return [i, nums_dict[remainder]]
        
print(twoSum([2,7,11,15],9))  
        
        
    