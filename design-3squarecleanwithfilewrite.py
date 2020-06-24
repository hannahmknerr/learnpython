def answerkey():
    """
    importing the text file that will be the answer key to my game
    """
    outfile = open("newpuzzlefilefromhannah", "w")
    outfile.write("her:female\n")
    outfile.write("era:time\n")
    outfile.write("rat:rodent\n")
    outfile.close()

    infile = open("newpuzzlefilefromhannah", "r")
    answerkey = infile.readlines()
    return answerkey

def welcome():
    """
    welcome message and clues
    """
    print("\n ---- Welcome to 3 Square!! ---- \n")
    for i in range(3):
        print("  |   |        ", i+1, ".", ("".join(answerkey())).split('\n')[i][4:])
    print("\n")

def inputs():
    """
    building the input requests between turns
    """
    options = ['q','1','2','3']
    guesswhile = 0
    while guesswhile == 0:
        guessnum = input("q123>").lower()
        if guessnum in options:

            guesswhile = 1
        else:
            print("try that again?")
    return guessnum

def inputsguess():
    """
    taking inputs of the actual guess word
    """
    guesstracker = 0
    while guesstracker == 0:
        theirguess = input("Guess:").lower()
        print()
        if len(theirguess) == 3:
            guesstracker = 1
        else:
            print("try a 3 letter word...")
    return theirguess

def printing(guessnum, theirguess, basicall):
    """
    printing guesses in the box
    """
    if guessnum == '1':
        basic1 = [theirguess[0], " | " , theirguess[1], " | " , theirguess[2]]
        basicall.pop(0)
        basicall.insert(0, basic1)
    elif guessnum == '2':
        basic2 = [theirguess[0], " | " , theirguess[1], " | " , theirguess[2]]
        basicall.pop(1)
        basicall.insert(1, basic2)
    elif guessnum == '3':
        basic3 = [theirguess[0], " | " , theirguess[1], " | " , theirguess[2]]
        basicall.pop(2)
        basicall.insert(2, basic3)
    print("".join(basicall[0]), "1.".rjust(10), ("".join(answerkey())).split('\n')[0][4:])
    print("".join(basicall[1]), "2.".rjust(10), ("".join(answerkey())).split('\n')[1][4:])
    print("".join(basicall[2]), "3.".rjust(10), ("".join(answerkey())).split('\n')[2][4:], "\n")

def win(basicall):
    """
    determining when the game is won
    """
    basicallwork = ["".join(basicall[0]), "".join(basicall[1]), "".join(basicall[2])]
    basicallstep = "".join(basicallwork)
    basicallstep1 = basicallstep.split()
    while basicallstep1.count("|") > 0:
        basicallstep1.pop(basicallstep1.index("|"))
    basicallfinal = "".join(basicallstep1)

    gone = ("".join(answerkey())).split('\n')[0][0:3]
    gtwo = ("".join(answerkey())).split('\n')[1][0:3]
    gthree = ("".join(answerkey())).split('\n')[2][0:3]
    gstep = [gone, gtwo, gthree]
    gfinal = "".join(gstep)

    if basicallfinal == gfinal:
        winner = True
        print("\nYou solved it!\n")
    else:
        winner = False
    return winner

def main():
    """
    main body of the game
    """
    basic1 = "  |   |        "
    basic2 = "  |   |        "
    basic3 = "  |   |        "
    basicall = [basic1,basic2,basic3]
    longermemory = []
    welcome()
    winner = False
    while winner == False:
        guessnum = inputs()
        quittingform(guessnum)
        theirguess = inputsguess()
        printing(guessnum, theirguess, basicall)
        winner = win(basicall)

def quittingform(guessnum):
    """
    quit file for if q is selected
    """
    if guessnum == 'q':
        gone = ("".join(answerkey())).split('\n')[0][0:3]
        gtwo = ("".join(answerkey())).split('\n')[1][0:3]
        gthree = ("".join(answerkey())).split('\n')[2][0:3]
        altogether = [gone, gtwo, gthree]
        jumper = 0
        jumpoptions = [2,5,8]
        print()
        for a in altogether:
            for b in a:
                if jumper in jumpoptions:
                    print(b)
                    jumper +=1
                else:
                    print(b, "| ", end="")
                    jumper +=1
        print()

        quit()

main()
