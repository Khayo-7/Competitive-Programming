from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positives = []
        negatives = []
        answer = []

        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
        
        for positive, negative in zip(positives, negatives):
            answer.append(positive)
            answer.append(negative)
        
        return answer
