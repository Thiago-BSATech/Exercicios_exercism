"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):

    if card in ('K', 'Q', 'J'):
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)




def higher_card(card_one, card_two):
   
    def value_of_cardv2(card):
        if card in ('K', 'Q', 'J'):
            return 10
        elif card == 'A':
            return 1
        else:
            return int(card)
    def returning_two_values(value_one, value_two):
        return value_one, value_two
        
    if value_of_cardv2(card_one) == value_of_cardv2(card_two):
        return returning_two_values(card_one, card_two)
    elif value_of_cardv2(card_one) >= value_of_cardv2(card_two):
        return card_one
    elif value_of_cardv2(card_two) >= value_of_cardv2(card_one):
        return card_two
        

    


def value_of_ace(card_one, card_two):

    if card_one == 'A' or card_two == 'A':
        return 1
        


    total = value_of_card(card_one) + value_of_card(card_two)

    if card_one == 'A' and card_two == 'A':
        total = 12
    
    if total + 11 <= 21:
        return 11
    else:
        return 1
    

  


def is_blackjack(card_one, card_two):

    total = value_of_card(card_one) + value_of_card(card_two)

    if 'A' in (card_one, card_two):
        if card_one == 'A' and card_two == 'A':
            total = 12
        elif card_one == 'A' and value_of_card(card_two) == 10:
            return True
        elif card_two == 'A' and value_of_card(card_one) == 10:
            return True
    
    
    if card_one == 'A' and card_two == 'A':
        total = 12
    
    
    if total == 21:
        return True 
    else: 
        return False
    


def can_split_pairs(card_one, card_two):

    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False

    


def can_double_down(card_one, card_two):
    
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)

