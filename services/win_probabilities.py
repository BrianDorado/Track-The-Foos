from player_ratings import Caden, Brian, Cambree, Logan, Ashlynn, Taylor, Jothan


player_a =
player_b =


def prob_player_wins(player_a, player_b) -> list:
    rating_a = player_a.elo_rating
    rating_b = player_b.elo_rating

    probability_a = 1/(1 + 10 ** ((rb - ra)/400))
    probability_b = 1 - probability_a
    return [probability_a, probability_b]