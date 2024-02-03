class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        total_identical_pairs = 0
        
        for i in set(nums):
            count = nums.count(i)
            identical_pairs = count*(count - 1) // 2
            total_identical_pairs += identical_pairs
        
        return total_identical_pairs