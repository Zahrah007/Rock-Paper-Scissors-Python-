import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'
emojis = {'r':'🪨', 's':'✂️', 'p':'📄'}
choices = tuple(emojis.keys())

def get_choice():
    while True:
        choice = input('Rock, Paper, or Scissors? (r/p/s): ').lower()
        if choice in choices:
            return choice
        else:
            print ('Please enter a valid choice!')

def display_choice(choice, comp_choice):
    print(f'You chose: {emojis[choice]}')
    print(f'Computer chose: {emojis[comp_choice]}')

def determine_winner(choice, comp_choice):
    if choice == comp_choice:
        print('Tie!')
    elif (
        (choice == PAPER and comp_choice == ROCK) or
        (choice == SCISSOR and comp_choice == PAPER) or
        (choice == ROCK and comp_choice == SCISSOR)):
        print('You win!')
    else:
        print('You lose!')

def play_game():
    while True:
        choice = get_choice()

        comp_choice = random.choice(choices)

        display_choice(choice, comp_choice)

        determine_winner(choice, comp_choice)

        should_continue = input('Do you want to continue? (y/n): ').lower()
        if should_continue == 'n':
            break

play_game()