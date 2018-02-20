#Copyright 2018 Brennan McMicking

def main():
    print "the number of possible arrangements for a deck of cards is:\n" + str(factorial(52))

def factorial(n):
    if n < 1:
        return 1
    else:
        rN = n*factorial(n-1)
        return rN


if __name__ == "__main__":
    main()
