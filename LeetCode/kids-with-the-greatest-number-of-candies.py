from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        answer = []
        max_candies = max(candies)
        
        for candy in candies:
            if candy + extraCandies >= max_candies: 
                answer.append(True)
            else:
                answer.append(False)

        return answer
