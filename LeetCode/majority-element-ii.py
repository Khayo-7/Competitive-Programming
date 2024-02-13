from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        record = {}

        for num in nums:
            if num in record:
                record[num] += 1
            else:            
                record[num] = 1
              
        return [num for num in record if record[num] > len(nums)/3]
