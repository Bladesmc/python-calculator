# This file does all the fun math and returns it back to the command line or GUI.
import factorial as f

def calculate(inp):
    inp = inp.replace(" ", "")
    o = ""
    if inp[-1] == "!":
        o = get_factorial(inp[:-1])
    elif inp.find("^") is not -1:
        o = get_exponent(inp)
    elif inp.find("%") is not -1:
        o = get_modulo(inp)
    else:
        o = "[ERROR] Could not determine mathematical function."
    return str(o)


def get_factorial(n):
    error = False
    o = ""
    ni = int()
    try:
        ni = int(n)
    except ValueError:
        error = True
        o = "[ERROR] Invalid number. {fact}"

    if not error:
        try:
            o = n + "! = " + str(f.factorial(ni))
        except RuntimeError:
            o = "[ERROR] Number exceeded maximum size. {fact}"

    return o


def get_exponent(s):
    error = False
    pwr = s.find("^")
    base, exp = int(),int()
    o = ""
    try:
        base = int(s[:pwr])
    except ValueError:
        o = "[ERROR] Invalid base. {exp}"
        error = True
    try:
        exp = int(s[pwr + 1:])
    except ValueError:
        o = "[ERROR] Invalid exponent. {exp}"
        error = True
    if not error:
        o = str(base ** exp)

    return o


def get_modulo(s):
    error = False
    mod = s.find("%")
    dividend, divisor = int(),int()
    o = ""
    try:
        dividend = int(s[:mod])
    except ValueError:
        o = "[ERROR] Invalid dividend. {mod}"
        error = True
    try:
        divisor = int(s[mod + 1:])
    except ValueError:
        o = "[ERROR] Invalid divisor. {mod}"
        error = True

    if not error:
        o = str(dividend % divisor)

    return o
