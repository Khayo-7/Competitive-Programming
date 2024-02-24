class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        players = list(range(1, n + 1))
     
        k -= 1
        index = 0

        while len(players) > 1:
            index = (index + k) % len(players)
            players.pop(index)

        return players[0]      