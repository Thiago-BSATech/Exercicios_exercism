"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):

    list = [number, number + 1, number + 2]
    return list


def concatenate_rounds(rounds_1, rounds_2):

    new_list = []
    for item in rounds_1, rounds_2:
        for i in item:
            new_list.append(i)
    return new_list

    


def list_contains_round(rounds, number):

    for i in rounds:
        if i == number:
            return True
    return False
    


def card_average(hand):

    return sum(hand) / len(hand)



def approx_average_is_average(hand):
    # PARA PERGUNTAR... 

    
    
    average_all_hand = card_average(hand)
    average_first_last = (hand[0] + hand[-1]) / 2

    # IA --
    sorted_hand = sorted(hand)
    n = len(sorted_hand)
    if n % 2 == 1:
        median = sorted_hand[n // 2]  
    else:
        median = (sorted_hand[n // 2 - 1] + sorted_hand[n // 2]) / 2  

    
    return average_all_hand == average_first_last or average_all_hand == median
    # -- IA


def average_even_is_average_odd(hand):

    handEven = []
    handOdd = []
    
    for index in hand:
        if index % 2 == 0:
            handEven.append(index)
        elif index % 2 != 0:
            handOdd.append(index)

    try:
        av_even = sum(handEven) / len(handEven) 
        av_odd = sum(handOdd) / len(handOdd)
    except:
        av_even = 0
        av_odd = 0

    return av_even == av_odd
            
    

def maybe_double_last(hand):

    if hand[-1] == 11:
        hand[-1] = hand[-1] + 11
    return hand

    pass