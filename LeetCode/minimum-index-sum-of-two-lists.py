from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        answer = []
        min_idx = float('inf')
        list1_new = {}

        for i in range(len(list1)):
            list1_new[list1[i]] = i

        for i in range(len(list2)):

            word = list2[i]
            if word in list1_new:
                if i + list1_new[word] < min_idx:
                    answer = [word]
                    min_idx = i + list1_new[word]

                elif i + list1_new[word] == min_idx:
                    answer.append(word)

        return answer


        # for i in range(len(list1)):
        #     word = list1[i]
        #     if word in list2:
        #         if i + list2.index(word) < min_idx:
        #             answer = [word]
        #             min_idx = i + list2.index(word)

        #         elif i + list2.index(word) == min_idx:
        #             answer.append(word)

        # return answer