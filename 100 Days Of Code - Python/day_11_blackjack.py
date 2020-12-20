############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
import os

# pylint: disable anomalous-backslash-in-string

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def clear():
    os.system('cls')


def initialize_hands():
    dealer_hand.append(draw_card())
    dealer_hand.append(draw_card())
    player_hand.append(draw_card())
    player_hand.append(draw_card())


def display_hands(reveal_dealer=False):
    dealer_masked_hand = ['X']
    dealer_masked_hand += dealer_hand[1:]
    dealers_masked_count = sum(dealer_hand[1:])
    dealers_hand_count = sum(dealer_hand)
    players_hand_count = sum(player_hand)
    if reveal_dealer:
        print(f'Dealers Hand [{dealers_hand_count}]: {dealer_hand}')
    else:
        print(f'Dealers Hand [{dealers_masked_count}]: {dealer_masked_hand}')
    print(f'Players Hand [{players_hand_count}]: {player_hand}')


def calculate_hand(hand):
    hand_count = sum(hand)
    current_hand = hand
    if hand_count <= 21:
        return hand_count
    while sum(current_hand) > 21:
        try:
            index = current_hand.index(11)
            current_hand[index] = 1
            if sum(current_hand) < 21:
                return sum(current_hand)
        except:
            return sum(current_hand)


def continue_game():
    response = input('Would you like to play another hand? [1]Yes [2]No\n')
    try:
        if int(response) == 1:
            return True
    except:
        return False


def display_winner():
    player_score = sum(player_hand)
    if player_score > 21:
        print('Bust.  Sorry you lose\n')
        display_hands()
        return
    dealer_score = sum(dealer_hand)
    while dealer_score < 17 and dealer_score <= 21:
        dealer_hand.append(draw_card())
        dealer_score = sum(dealer_hand)
    if dealer_score > 21:
        print('Dealer Bust: You Win!')
    elif dealer_score > player_score:
        print('Dealer Wins!')
    elif player_score > dealer_score:
        print('You Won!')
    else:
        print('Tie')
    display_hands(True)


playing = True
while playing:
    clear()
    dealer_score = 0
    dealer_hand = []
    player_score = 0
    player_hand = []
    player_choosing = True
    print(logo)
    initialize_hands()
    display_hands()
    while player_choosing:
        print('Hit or Stand?')
        try:
            player_choice = input('[1]Hit [2]Stand:  ')
            print('\n')
            if int(player_choice) == 1:
                player_hand.append(draw_card())
                if calculate_hand(player_hand) > 21:
                    player_choosing = False
                    break
                display_hands()
                continue
            else:
                player_choosing = False
        except:
            player_choosing = False

    display_winner()

    playing = continue_game()
