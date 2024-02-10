from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        answer = []
        ln = len(nums)//2

        for i in range(ln):
            answer.append(nums[i])
            answer.append(nums[i + ln])
            
        return answer