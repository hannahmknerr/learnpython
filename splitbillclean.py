def splitbill():
    """ Split a bill with tip between a number of people"""

    print("Bill amount:")
    pre = float(input())
    print("Number of People")
    people = float(input())
    print("Percent Tip")
    percent = float(input())/100

    tip = round((pre*percent), +2)

    post = round(((1+percent)*pre), +2)



    total = round(pre*(1+(percent))/people, +2)

    print("The tip is", "$", tip)
    print("The total cost is $", post)
    print("The cost per person is $", total)

splitbill()
