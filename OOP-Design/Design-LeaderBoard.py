"""Design a Leaderboard class, which has 3 functions:

    1. addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
    2. top(K): Return the score sum of the top K players.
    3. reset(playerId): Reset the score of the player with the given id to 0 
    (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.

    Note: Initially, the leaderboard is empty.
"""

from sortedcontainers import SortedDict

class Leaderboard:
    def __init__(self):
        self.scores = {}                    # {playerId: score}
        self.sorted_scores = SortedDict()   # {score: no of players with score}

    def add_score(self, playerId: int, score: int) -> None:
        """
            - check if playerId exists in self.scores(new player or not)
            - if not, set self.scores[playerId] and add 1 to self.sorted_scores[-score]
            - if exists, add new score to existing score in self.scores, and update no of players in self.sorted_scores
        """
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sorted_scores[-score] = self.sorted_scores.get(-score, 0) + 1
        else:
            prev_score = self.scores[playerId]
            new_score = prev_score + score

            # update no of players in self.sorted_scores[-score]
            if self.sorted_scores[-score] == 1:
                del self.sorted_scores[-score]
            else:
                self.sorted_scores[-score] -= 1

            # update self.scores and self.sorted_scores with new score total
            self.scores[playerId] = new_score
            self.sorted_scores[-new_score] = self.sorted_scores.get(-new_score, 0) + 1

    def top(self, K: int) -> int:
        count, total = 0, 0

        for k, v in self.sorted_scores.items():
            players = v

            for _ in range(players):
                total += (-k)
                count += 1

                if count == K:
                    break
            if count == K:
                break
        return total

    def reset(self, playerId: int) -> None:
        score = self.scores[playerId]

        # reduce score:players count
        if self.sorted_scores[-score] == 1:
            del self.sorted_scores[-score]
        else:
            self.sorted_scores[-score] -= 1
        
        # delete player from leaderboard
        del self.scores[playerId]


leaderboard = Leaderboard()
leaderboard.addScore(1,73)
leaderboard.addScore(2,56)
leaderboard.addScore(3,39)
leaderboard.addScore(4,51)
leaderboard.addScore(5,4)
print(leaderboard.top(1))
leaderboard.reset(1)
leaderboard.reset(2)
leaderboard.addScore(2,51)
print(leaderboard.top(3))