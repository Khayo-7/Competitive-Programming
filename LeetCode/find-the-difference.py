class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # index = 0
        # s_len = len(s)

        # s_sorted = sorted(list(s))
        # t_sorted = sorted(list(t))
        
        # while index < s_len:
        #     if s_sorted[index] != t_sorted[index]:
        #         break
        #     else:
        #         index += 1
        
        # return t_sorted[index]
        
        # index = 0
        # diff = 0
        # s_len = len(s)

        # while index < s_len:
        #     diff += (ord(t[index]) - ord(s[index]))
        #     index += 1
        
        # return chr(ord(t[index]) + diff)
        
        diff = 0
        for char in s + t:
            diff ^= ord(char)

        return chr(diff)
