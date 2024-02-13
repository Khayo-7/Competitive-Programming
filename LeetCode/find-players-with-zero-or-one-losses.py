class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        record = {}
        all_win = set()
        lost_one = set()

        for winner, loser in matches:

            if not winner in record:
                record[winner] = 0
                all_win.add(winner)
                      
            if (not loser in record) or (record[loser] == 0):
                record[loser] = 1
                lost_one.add(loser)
                all_win.discard(loser)
            else:
                record[loser] += 1
                lost_one.discard(loser)
                all_win.discard(loser)
            #2
            # if not loser in record:
            #     record[loser] = 1
            #     lost_one.add(loser)
            # else:
            #     if record[loser] == 0:
            #         lost_one.add(loser)
            #         all_win.discard(loser)
            #     else:
            #         lost_one.discard(loser)
            #     record[loser] += 1
        #3
        #     if not winner in record:
        #         record[winner] = 0
        #     if not loser in record:
        #         record[loser] = 1
        #     else:
        #         record[loser] += 1
       
        # for player, loses in record.items():
        #     if loses == 0:
        #         all_win.add(player)
        #     elif loses == 1:
        #         lost_one.add(player)

        return [sorted(list(all_win)), sorted(list(lost_one))]

