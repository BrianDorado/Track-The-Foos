from importlib.metadata import pass_none
from player_ratings import Caden, Brian, Cambree, Logan, Jothan, Ashlynn, Taylor


def calculate_elo(player_rating: float, opponent_rating: float, player_won: bool, k: int = 32) -> float:
    """
    Calculate the new ELO rating for a player after a match.

    Parameters:
        player_rating (float): The current ELO rating of the player.
        opponent_rating (float): The current ELO rating of the opponent.
        player_won (bool): True if the player won the match, False if they lost.
        k (int): The K-factor, which determines the maximum rating change per match (default is 32).

    Returns:
        float: The player's new ELO rating.

    Docs: https://en.wikipedia.org/wiki/Elo_rating_system
    """


    ra = player_a.elo_rating
    # Rating of player A

    rb =
    # Rating of player B


    def prob_player_wins(rating_a, rating_b) -> list:
        probability_a = 1/(1 + 10 ** ((rating_b - rating_a)/400))
        probability_b = 1 - probability_a
        return [probability_a, probability_b]







    expected_outcome = 1 / (1 + 10 ** ((opponent_rating - player_rating) / 400))


    actual_outcome = 1 if player_won else 0


    new_rating = player_rating + k * (actual_outcome - expected_outcome)

    return new_rating
