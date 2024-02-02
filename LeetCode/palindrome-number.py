class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x != 0 and x%10 == 0):
            return False
     
        x_ = 0
        while x_ < x:            
            x_ = (x_*10) + (x%10)
            x //= 10
        
        return x == x_ or x == x_//10
    
        # xx = str(x)
        # mid = len(xx) // 2 
        # return xx[:mid] == xx[:mid:-1]

        # return str(x) == str(x)[::-1]