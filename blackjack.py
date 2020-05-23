from random import *
def main():
    games = 1
    wins = 0
    loses = 0
    while games < 11:
        print("Game", games)
        print()
        limit = 15
        score = oneHand(limit)
        print(score)
        print()
        games = games + 1
        if score == 21:
            print(":)")
            print()
            wins = wins + 1
        if score > 21:
            print(":(")
            print()
            loses = loses + 1
    print(wins, "wins and", loses, "loses")



def oneHand(limit):
    cards = 1,2,3,4,5,6,7,8,9,10
    first = choice(cards)
    second = choice(cards)
    print()
    print("First two cards are:", first, second)
    total = first + second
    while total < limit:
        next = choice(cards)
        total = total + next
        print("You drew a", next, ": total is now", total)
    if total > 21:
        print("You LOSE!")

    return total

main()
