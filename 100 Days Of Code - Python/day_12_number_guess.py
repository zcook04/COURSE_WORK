from random import randint
import os

logo = r'''
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_| 
  '''


def get_number():
    return randint(1, 100)


def clear_screen():
    os.system('cls')


def get_difficulty():
    try:
        print('Select Difficulty')
        choice = int(input('[1]Easy [2]Medium [3]Hard :  '))
        if choice == 1:
            print('Easy mode engaged.\n\n')
            return 10
        elif choice == 2:
            print('Normal mode engaged.\n\n')
            return 7
        elif choice == 3:
            print('Hard mode engaged. Good Luck!\n\n')
            return 5
        else:
            clear_screen()
            print(logo)
            print('Please select either [1]Easy [2]Medium or [3]Hard')
            get_difficulty()
    except:
        clear_screen()
        print(logo)
        print('Please select either [1]Easy [2]Medium or [3]Hard')
        get_difficulty()


def get_guess(attempts):
    print(
        f'You have {attempts} attempts remaining.  Guess a number between 1 and 100')
    try:
        guess = int(input('Guess:  '))
        print('\n')
        return guess
    except:
        get_guess(attempts)


def check_guess(guess, answer):
    if guess == answer:
        return False
    else:
        return True


def evaluate_guess(guess, answer):
    if guess < answer:
        print('Your guess was lower then the answer, try again')
    else:
        print('Your guess was higher then the answer, try again')


def get_result(guess, answer, lives):
    if guess == answer and lives > 0:
        print('YOU WIN')
    else:
        print('Sorry you lose')

    play_again = int(input('\nWould you like to play again? [1]Yes [2]No: '))
    if play_again == 1:
        clear_screen()
        game_start()


def game_start():
    print(logo)
    lives = get_difficulty()
    answer = get_number()
    game_running = True
    while game_running:
        current_guess = get_guess(lives)
        game_running = check_guess(current_guess, answer)
        if not game_running:
            break
        else:
            evaluate_guess(current_guess, answer)
            lives -= 1
            if lives < 1:
                break
    get_result(current_guess, answer, lives)


if __name__ == '__main__':
    game_start()
