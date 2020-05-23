def main():
    left = int(input("How many pages left to read?:"))
    days = int(input("How many days until it is due?:"))
    suggest = left/days

    pages = left
    for i in range(days):
        print("You've got", pages, "pages left and", days, "days to go. Try reading", suggest, "pages per day." )
        daily = int(input("How many pages did you read today?:"))
        pages = pages - daily
        days = days - 1
        if days > 0:
            suggest = pages/days
        else:
            if pages > 0:
                print("You didn't finish in time")
            if pages == 0:
                print("Good work!")
            if pages < 0:
                print("Overachiever!")

main()
