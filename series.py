def main():
    terms = int(input("How many terms?: "))
    sum = 0

    for i in range(terms):
        num = 1 / ((i+1) ** 2)
        sum = num + sum
        print(round(sum, +4))

main()
