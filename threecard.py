from random import *
def main():

    end = 0
    round = 1
    while end == 0:
        print("Round", round)
        pick = getPick()
        print("You chose: %s" % (pick))
        options = 'A', 'B', 'C'
        queen = choice(options)
        if queen == pick:
            print("You win!")
            print("It only took", round, "rounds!")
            end = 1
        else:
            print("Sorry. The Queen was", queen)
            round = round + 1
def getPick():
    answer = ''
    selection = input("Where is the Queen of Hearts? [A, B, C]:")
    if selection == 'A':
        answer = 'A'
    elif selection == 'B':
        answer = 'B'
    elif selection == 'C':
        answer = 'C'
    else:
        value = 0
        while value == 0:
            selection = input("Please enter A, B, or C!!:")
            if selection == 'A':
                value = 1
                answer = 'A'
            elif selection == 'B':
                value = 1
                answer = 'B'
            elif selection == 'C':
                value = 1
                answer = 'C'
            else:
                value = 0
    return answer
main()
