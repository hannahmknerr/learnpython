from random import *
def main():

    rolls = int(input("How many rolls?"))

    list = 'left', 'right', 'back', 'up', 'snout', 'jowls', 'touching'
    values = 1,1,5,5,10,15,0

    value_total = 0
    for i in range(rolls):
        roll_one = choice(list)
        roll_two = choice(list)

        in_one = list.index(roll_one)
        in_two = list.index(roll_two)

        value_one = values[in_one]
        value_two = values[in_two]

        if (roll_one == roll_two) and (roll_one == 'left' or roll_one == 'right'):
            value_total = 1
        elif roll_one == roll_two:
            value_total = (value_one) * 4
        elif value_two == 0 or value_one == 0:
            value_total = 0
        elif (roll_two == 'left' and roll_one == 'right') or (roll_one == 'left' and roll_two == 'right'):
            value_total = 0
        else:
            value_total = value_one + value_two

        print("Roll:", roll_one, roll_two)
        print("Values:", value_one, value_two)
        print("Score:", value_total)

main()
