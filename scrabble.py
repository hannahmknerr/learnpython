def main():
    """scrabble score simplified"""

    letters = list("abcdefghijklmnopqrstuvwxyz")
    scores = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]

    word = input("What's your word?:")
    sum = 0
    for i in word:
        place = letters.index(i)

        sum = scores[place] + sum

        print("letter: ", i, "(index:", "{:<2d}".format(place), ") score for letter:", scores[place])
    print()
    print("Your total score is:", sum)

main()
