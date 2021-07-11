from random import randint
from os import system, name


MAX_GUESS = 3
MIN_NUM = 1
MAX_NUM = 20


def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == '__main__':


    clear()


    print('''
    You approach and old bridge spanning an enormous gorge.  An old man greets you

    ''')

    player_name = input('    What is your name?  ')

    print(f'''

    Ok {player_name}, let us play a little game. I am thinking of a number
    between {MIN_NUM} and {MAX_NUM}.  You will have {MAX_GUESS} tries to guess the right number.

    
    I you guess correctly, you may pass.  If you fail... Let's just say,
    It is a lonng way to the bottom...

    ''')

    print('\n\n')

    number = randint(MIN_NUM, MAX_NUM)
    guessed = False

    for turn in range(MAX_GUESS):

        print(f'    Guess #{turn + 1}')
        player_num = input('    Guess a number:  ')
        try:
            player_num = int(player_num)
        except ValueError:
            print(f'    {player_num} is not a number\n')
            continue

        if player_num < number:
            print('    That number is too low.\n')

        if player_num > number:
            print('    That number is too high.\n')

        if player_num == number:
            print('    That is correct.')
            guessed = True
            break


    if guessed:
        print(f'''

    The old man moves aside, gesturing for you to continue on your way.
    As you pass, you hear the old man cry out,

    Good luck, {player_name}, you're going to need it where you're going!
        
        ''')
    else:
        print(f'''

    You hear mad cackling as you feel yourself launched into the air.
    Disoriented, you look up, and watch as the bridge fades from view...

        ''')
