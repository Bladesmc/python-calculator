import factorial as f


def main():
    while True:
        try:
            inp = int(raw_input("enter a valid number and then press <ENTER>:\t"))
            break
        except ValueError:
            print("Error: Invalid number. Try again...")

    print "the factorial of " + str(inp) + " is\t" + str(f.factorial(inp))


if __name__ == "__main__":
    main()
