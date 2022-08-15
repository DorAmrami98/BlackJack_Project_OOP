import random

"""
Given strategies 
"""


def strategy1(player_hand, dealer_hand):
    player_value = player_hand.value()
    dealer_value = dealer_hand.value()

    if player_value < dealer_value:
        return 'hit'

    if player_hand.soft:
        if player_value < 17:
            return 'hit'
        elif player_value > 18:
            return 'stand'
        else:
            if random.choice([0, 1]):
                return 'hit'
            else:
                return 'stand'
    else:  # hard hand
        if player_value < 11:
            return 'hit'
        elif player_value > 17:
            return 'stand'
        else:
            return 'hit'


def strategy3(player_hand, dealer_hand):
    p_value = player_hand.value()
    d_value = dealer_hand.value()
    p_soft = player_hand.soft
    d_soft = dealer_hand.soft
    p_hard = not player_hand.soft
    d_hard = not dealer_hand.soft

    if 17 <= d_value <= 21:  # Dealer soft hand
        if p_value < d_value:
            return 'hit'
    elif 7 <= d_value <= 11:
        if p_value <= d_value or 12 <= p_value <= 15:
            return 'hit'
    elif d_value < 7:
        if p_value < 12:
            return 'hit'
        elif p_soft and p_value < 16:
            return 'hit'

    if d_hard and 12 <= d_value <= 16:  # Dealer hard hand
        if p_value < d_value:
            return 'hit'
        elif p_soft and p_value <= 16:
            return 'hit'

    if d_soft and 12 <= d_value <= 16:
        if p_value <= 12:
            return 'hit'
        elif p_soft and p_value <= 18:
            return 'hit'
    return 'stand'


def strategy_dealer(d_hand):
    """
     The dealer strategy
    """
    if d_hand.value() < 17:
        return "hit"
    else:
        return "stand"
