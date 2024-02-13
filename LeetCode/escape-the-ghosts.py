from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        player_move = abs(target[0]) + abs(target[1])

        for ghost in ghosts:
            ghost_move = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if  ghost_move <= player_move:
                return False

        return True