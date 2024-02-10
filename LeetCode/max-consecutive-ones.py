class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_cons = 0
        cons = 0

        for num in nums:
            if num:
                cons += 1
                continue
            
            max_cons = max(max_cons, cons)
            cons = 0
        
        max_cons = max(max_cons, cons)
        return max_cons