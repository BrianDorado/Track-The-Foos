

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

    expected_outcome = 1 / (1 + 10 ** ((opponent_rating - player_rating) / 400))


    actual_outcome = 1 if player_won else 0


    new_rating = player_rating + k * (actual_outcome - expected_outcome)

    return new_rating
