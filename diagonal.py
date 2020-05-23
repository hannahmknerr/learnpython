def main():
    """diagonal writing!"""

    words = str(input("Enter Text to be DIAGONALIZED:"))
    digits = int(input("How many characters per line?:"))
    num = 0
    diag = 0
    d2 = digits
    for i in words:
        if diag < len(words):
            print(" " * num, words[diag:d2])
            num = num + 1
            diag = diag + digits
            d2 = d2 + digits

main()
