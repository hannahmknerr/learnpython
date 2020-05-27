def quiz():
    print()
    print("Hello and welcome to HMK's buzzfeed based Knerr Family Quiz!")
    print()
    token = 0
    mom = 0
    dad = 0
    courtney = 0
    aidan = 0
    hannah = 0
    winners = []

    while token == 0:

        yes_or_no = input("Would you like to play?:")
        normalized = [yes_or_no.rstrip('.,!?').lower()]

        if normalized[0] == "yes":
            print()
            print("Hooray! Let's go:")
            token = 2
        elif normalized[0] == "no":
            print()
            print("Alright. Maybe next time.")
            token = 1
        else:
            print()
            print("Don't think that's an answer? Try yes or no!")
            print()
            token = 0

    while token == 1:
        print()
        print("It's over!")
        exit()

    while token == 2:
        print()
        qone = input("Question 1: What are your dietary preferenes? \n A) Vegan \n B) Vegetarian \n C) Something in between \n D) Omnivore \n Response:")
        qone_normalized = [qone.rstrip('.,!?()').lower()]
        if qone_normalized[0] == 'a':
            courtney = courtney + 1
            token = 3
        elif qone_normalized[0] == 'b':
            aidan = aidan + 1
            token = 3
        elif qone_normalized[0] == 'c':
            mom = mom + 1
            dad = dad + 1
            token = 3
        elif qone_normalized[0] == 'd':
            hannah = hannah + 1
            token = 3
        else:
            print("Not a valid answer!! Try A, B, C, or D?")
            token = 2

    while token == 3:
        print()
        qtwo = input("Question 2: Who is your favorite dog? \n A) Abby \n B) Max \n C) Lily \n D) Sammy \n Response:")
        qtwo_normalized = [qtwo.rstrip('.,!?()').lower()]
        if qtwo_normalized[0] == 'c':
            courtney = courtney + 1
            token = 4
        elif qtwo_normalized[0] == 'a':
            dad = dad + 1
            token = 4
        elif qtwo_normalized[0] == 'd':
            hannah = hannah + 1
            aidan = aidan + 1
            token = 4
        elif qtwo_normalized[0] == 'b':
            mom = mom + 1
            token = 4
        else:
            print("Not a valid answer!! Try A, B, C, or D?")
            token = 3

    while token == 4:
        print()
        qthree = input("Question 3: Where would you take your partner on a date? \n A) Swimming Pool \n B) Birding \n C) Brewery \n D) Rhett Miller Concert \n Response:")
        qthree_normalized = [qthree.rstrip('.,!?()').lower()]
        if qthree_normalized[0] == 'b':
            courtney = courtney + 1
            token = 5
        elif qthree_normalized[0] == 'a':
            aidan = aidan + 1
            token = 5
        elif qthree_normalized[0] == 'c':
            hannah = hannah + 1
            dad = dad + 1
            token = 5
        elif qthree_normalized[0] == 'd':
            mom = mom + 1
            token = 5
        else:
            print("Not a valid answer!! Try A, B, C, or D?")
            token = 4

    while token == 5:
        print()
        qfour = input("Question 4: How much python do you know? \n A) I have a Phd \n B) How much can you learn in a month? \n C) Intro CS \n D) Snakes? \n Response:")
        qfour_normalized = [qfour.rstrip('.,!?()').lower()]
        if qfour_normalized[0] == 'a':
            dad = dad + 1
            token = 6
        elif qfour_normalized[0] == 'c':
            aidan = aidan + 1
            courtney = courtney + 1
            token = 6
        elif qfour_normalized[0] == 'b':
            hannah = hannah + 1
            token = 6
        elif qfour_normalized[0] == 'd':
            mom = mom + 1
            token = 6
        else:
            print("Not a valid answer!! Try A, B, C, or D?")
            token = 5

        while token == 6:
            print()
            qfive = input("Question 5: What is your favorite kind of book? \n A) TV \n B) Romance \n C) YA \n D) Dogs \n Response:")
            qfive_normalized = [qfive.rstrip('.,!?()').lower()]
            if qfive_normalized[0] == 'a':
                courtney = courtney + 1
                token = 7
            elif qfive_normalized[0] == 'b':
                aidan = aidan + 1
                token = 7
            elif qfive_normalized[0] == 'c':
                hannah = hannah + 1
                dad = dad + 1
                token = 7
            elif qfive_normalized[0] == 'd':
                mom = mom + 1
                token = 7
            else:
                print("Not a valid answer!! Try A, B, C, or D?")
                token = 6

            while token == 7:
                print()
                qsix = input("Question 6: What's your favorite drink? \n A) Cosmo \n B) Margaritas \n C) Fireball Shots \n D) Wine \n Response:")
                qsix_normalized = [qsix.rstrip('.,!?()').lower()]
                if qsix_normalized[0] == 'd':
                    courtney = courtney + 1
                    token = 8
                elif qsix_normalized[0] == 'c':
                    aidan = aidan + 1
                    token = 8
                elif qsix_normalized[0] == 'b':
                    hannah = hannah + 1
                    dad = dad + 1
                    token = 8
                elif qsix_normalized[0] == 'a':
                    mom = mom + 1
                    token = 8
                else:
                    print("Not a valid answer!! Try A, B, C, or D?")
                    token = 7

    if token == 8:
        list = mom, dad, courtney, aidan, hannah
#        names = "mom", "dad", "courtney", "aidan", "hannah"
#        print(mom)
#        print(dad)
#        print(courtney)
#        print(aidan)
#        print(hannah)
        dictionary = {"mom":mom, "dad":dad, "courtney":courtney, "aidan":aidan, "hannah":hannah}
        print()
        print("Congrats! You are most like:")
        print()
        for z in dictionary:
            if dictionary.get(z) == max(list):
                winners.append(z)
                print(z)


#        print(dictionary['1'])
#        print(max(list))
#        for z in dictionary:
#            if z == max(list):
#                print("here")
#                winners = dictionary[z] + winners
                #print(dictionary[z] + "dictionary")
                #print(winners + "winners")
#        print(dictionary)

#    for i in list:
#        if i == max(list):
#            winners = winners + dictionary[i]
        print()
#        print("Congrats!!! You are the most like", winners)
        print()

        #print(names[list.index(max(list))])






quiz()
