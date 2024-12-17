# file to hold player data
from abc import ABC

class Player(ABC):
    def __init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference):
        self.elo_rating = elo_rating
        self.color_rating = color_rating
        self.pct_wins = pct_wins
        self.points_for = points_for
        self.points_against = points_against
        self.goal_difference = goal_difference


class Caden(Player):
    def __init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference):
        super().__init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference)

class Cambree(Player):
    def __init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference):
        super().__init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference)


class Logan(Player):
    def __init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference):
        super().__init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference)

class Brian(Player):
    def __init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference):
        super().__init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference)

class Jothan(Player):
    def __init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference):
        super().__init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference)

class Taylor(Player):
    def __init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference):
        super().__init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference)

class Ashlynn(Player):
    def __init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference):
        super().__init__(self, elo_rating, color_rating, pct_wins, points_for, points_against, goal_difference)

