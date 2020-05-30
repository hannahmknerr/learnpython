from random import *
def mastermind():
    colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']
    print()
    print("Welcome to")
    print()
    print("MASTERMIND")
    print()
    print("The rules of the game are simple.")
    print("Break the code by guessing 4 colors in the correct order.")
    print("The color options are\n", colors)
    print("Guessing a color in the code results in 'white' as feedback.")
    print("Guessing a color in the code in the correct position results in 'black' as feedback.")
    print("4 'blacks' and you've cracked the code!")
    print("Guess wisely though as you only have 12 turns to crack the code!")
    print("Let's get started!")

    code = {}
    for i in range(4):
        code[i] = choice(colors)
#    print(code)
    turns = 1
    while turns < 13:
        print('=' *50)
        print("Turn", turns,":")
        guess = input("Guess:").split(" ")
        guess_range = 0
        for i in guess:
            if i in colors:
                guess_range += 1
        if guess_range == 4:
            for i in code:
#                print(code[i], "!!!!!!!!!!!!!!!!!!!!!!!!")
                if code[i] == guess[i]:
                    print("black")
                    i_code = int(guess.index(code[i]))
                    guess.pop(i_code)
                    guess.insert(i_code, 'counted')

                elif code[i] in guess:
                    print("white")
                    it_code = int(guess.index(code[i]))
                    guess.pop(it_code)
                    guess.insert(it_code, 'counted2')

            if guess == ['counted','counted','counted','counted']:
                print("You cracked the code!")
                turns = 14
            turns += 1
        else:
            print("Please guess 4 colors! Options are:", colors)
    if turns == 13:
        print("Sorry. You lose!")
        print("The code was,", code)



mastermind()
