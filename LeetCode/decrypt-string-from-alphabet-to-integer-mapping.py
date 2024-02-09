class Solution:

    def freqAlphabets(self, s: str) -> str:

        def alpha_to_int(ch):
            return chr(int(ch) + 96)
      
        answer = ''
        # if len(s) == 1:
        #     answer = alpha_to_int(s[0])
        # elif len(s) == 2:
        #     answer = alpha_to_int(s[0]) + alpha_to_int(s[1])
        # else: 
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                answer = alpha_to_int(s[i-2] + (s[i-1])) + answer
                i -= 2
            else:
                answer = alpha_to_int(s[i]) + answer
            i -= 1
        return answer