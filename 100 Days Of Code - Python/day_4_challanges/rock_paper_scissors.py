# Create a rock paper scissors game against the computer.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def initial_prompt(win, lose, tie):
    print('Rock Paper Scissors.')
    print('----------------------------------------------------')
    print(f'Current Score -- WINS: {win}   LOSES: {lose}   TIES: {tie}')
    print('[1]: ROCK - Used to beat Scissors')
    print('[2]: PAPER - Used to beat Rock]')
    print('[3]: SCISSORS - Used to beat Paper')
    choice = int(input('Your Choice:   '))
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        return choice


def keep_playing(win, lose, tie):
    print('\n\nWould you like to play another game?')
    print('\n\n[1] Yes')
    print('\n\n[2] No')
    response = int(input('Your Choice: '))
    if response == 1:
        return True
    else:
        print(f'\n\n\n Final Score {win}-{lose}-{tie}')
        return False


def eval_winner(player1, player2):
    # 1 = Rock || 2 = Paper || 3 = Scissors
    if player1 == 1 and player2 == 1:
        return 3
    if player1 == 1 and player2 == 2:
        return 2
    if player1 == 1 and player2 == 3:
        return 1
    if player1 == 2 and player2 == 1:
        return 1
    if player1 == 2 and player2 == 2:
        return 3
    if player1 == 2 and player2 == 3:
        return 2
    if player1 == 3 and player2 == 1:
        return 2
    if player1 == 3 and player2 == 2:
        return 1
    if player1 == 3 and player2 == 3:
        return 3
    else:
        print('GAME LOGIC ERROR')
        return


def show_result(player1, player2, winner):
    print('\n\n')
    if winner == 1:
        print('You WIN!\n\n')
    elif winner == 2:
        print('You LOSE :(\n\n')
    else:
        print('IT WAS A TIE!!!\n\n')
    print('-----Player 1\'s Choice:\n')
    if player1 == 1:
        print(rock)
    if player1 == 2:
        print(paper)
    if player1 == 3:
        print(scissors)
    print('----Player 2\'s Choice')
    if player2 == 1:
        print(rock)
    if player2 == 2:
        print(paper)
    if player2 == 3:
        print(scissors)


game_loop = True
win = 0
lose = 0
tie = 0
while game_loop:
    players_choice = initial_prompt(win, lose, tie)
    computers_choice = random.randint(1, 3)
    winner = eval_winner(players_choice, computers_choice)
    if winner == 1:
        win += 1
    elif winner == 2:
        lose += 1
    else:
        tie += 1

    show_result(players_choice, computers_choice, winner)
    game_loop = keep_playing(win, lose, tie)
