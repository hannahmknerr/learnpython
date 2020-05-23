def main():
    """5 letter decoder"""

    text = str(input("input text:"))
    one = 0

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper = ''
    number = 0
    for x in letters:
        upper = upper + letters[number].upper()
        number = number + 1

    lupper = list(upper)
    both = lupper + letters

    nums = 0
    for i in text:
        for c in both:
            if i == c:
                print(i, end='')
                nums = nums + 1
                if nums%5 == 0:
                    print(" ", end='')
                if nums%25 ==0:
                    print()





    #print(final)

    #for i in text:
    #    print(text[one:one+5], end=' ')
    #    one = one + 5


    print()
main()
