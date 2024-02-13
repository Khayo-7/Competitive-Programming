from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        checked = False
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:

                if checked:
                    return False
                checked = True 

                if i==0 or nums[i-1]<=nums[i+1]:
                    nums[i]=nums[i+1]
                else:
                    nums[i+1]=nums[i]


        return True

    
       
            
