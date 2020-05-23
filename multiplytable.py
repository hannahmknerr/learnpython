def multiplytable():
    """input an integer and first 9 multiples will display"""

    print("Enter an integer factor:")
    number = int(input())

    numbers = 1,2,3,4,5,6,7,8,9

    mult = (numbers[0]*number), (numbers[1]*number), (numbers[2]*number), (numbers[3]*number), (numbers[4]*number), (numbers[5]*number), (numbers[6]*number),(numbers[7]*number),(numbers[8]*number)

    print("Factor", number)
    print( "n |", number, "* n \n ----- \n 1 |", mult[0], "\n 2 |", mult[1], "\n 3 |", mult[2], "\n 4 |", mult[3], "\n 5 |", mult[4], "\n 6 |", mult[5], "\n 7 |", mult[6], "\n 8 |", mult[7], "\n 9 |", mult[8])

multiplytable()
