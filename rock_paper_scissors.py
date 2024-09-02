# ROCK PAPER SCISSORS:
score = 0
def new_game():
    import random as rd
    global score

    choices = ['rock', 'paper', 'scissors']
    computer = rd.choice(choices)
    user = ''
    while user not in choices:
        user = input('enter your choice (rock/paper/scissors)').lower()

    print(f'YOU = {user}\nCOMP = {computer}')
    print('-------------------------------------------')

    if user == computer:
        print('TIE!..')

    elif user == 'rock':
        if computer == 'scissors':
            print('YOU WIN!..')
            score =+ 1
        else:
            print('YOU LOSE!..')
            score =- 1

    elif user == 'paper':
        if computer == 'rock':
            print('YOU WIN!..')
            score = + 1
        else:
            print('YOU LOSE!..')
            score = - 1
    elif user == 'scissors':
        if computer == 'paper':
            print('YOU WIN!..')
            score = + 1
        else:
            print('YOU LOSE!..')
            score = - 1
    print(f'SCORE = {score}')
    print('-------------------------------------------')
    play_again()

def play_again():
    user_response = input("Press 'ENTER' to start a New Game\nOR\nPress ANY other KEY to Quit.\n"
                          "-----------------------------------------")
    if len(user_response) == 0:
        new_game()

    else:
        print('Ooops! GOODBYE...!!!')

new_game()


