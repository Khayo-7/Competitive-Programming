from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        answer = []
        n = len(nums)

        for i in range(n):
            
            if nums[i] == 0:
                continue
           
            if i < n-1 and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

            answer.append(nums[i])

        return answer + [0]* (n - len(answer))


#         i = 0
#         while i<n:
#             if nums[i] == 0:
#                 i += 1
#                 continue
           
#             if i < n-1 and nums[i] == nums[i+1]:
#                 nums[i] *= 2
#                 nums[i+1] = 0

#             answer.append(nums[i])
#             i += 1

#         return answer + [0]* (n - len(answer))
