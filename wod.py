
from random import *
def wod():
    """comment for dad; workout program"""
    exercises = ["burpees","pushups","box jumps","deadlifts",
               "pullups","situps","squats","curls","toes to bar"]
    o = choice(exercises)
    exercises.remove(o)
    t = choice(exercises)
    exercises.remove(t)
    th = choice(exercises)
    exercises.remove(th)
    f = choice(exercises)

    on = randrange(8,16)
    ot = randrange(8,16)
    oth = randrange(8,16)
    of = randrange(8,16)

    print("1.",on, o)
    print("2.",ot, t)
    print ("3.", oth, th)
    print("4.", of, f)
wod()

def main():
    value = 0
    day = 6
    decide = ''
    print()
    print("Training Schedule for Week of OCT 6:")
    print("=" * 10)
    while value < 7:
        print("For October", day, ", 2019:")
        rest_day = "It's a rest day!!!"
        options = 'rest_day', 'wod', 'wod'
        value = value + 1
        day = day + 1
        decide = choice(options)
        if decide == 'wod':
            print("5 rounds of:")
            wod()
        elif decide == 'rest_day':
            print(rest_day)
        print()

main()
