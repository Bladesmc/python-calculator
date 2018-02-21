# Copyright 2018 Brennan McMicking
# TODO: support multiple operations at once

import factorial as f
from Tkinter import *


class Application(Frame):
    def get_factorial(self, n):
        error = False
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

        self.v.set(o)

    def get_exponent(self, s):
        error = False
        pwr = s.find("^")
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

        self.v.set(o)

    def calculate(self):
        inp = self.INPUT.get()
        if inp[-1] == "!":
            self.get_factorial(inp[:-1])
        elif inp.find("^") is not -1:
            self.get_exponent(inp)
        else:
            self.v.set("[ERROR] Could not determine mathematical function.")

    def createWidgets(self):
        self.GETFACT = Button(self, text="Calculate", fg="green", command=self.calculate)
        self.GETFACT.pack({"side": "left"})

        self.INPUT = Entry(self)
        self.INPUT.pack({"side": "left"})

        self.v = StringVar()

        self.OUTPUT = Label(self, textvariable=self.v, wraplength=1000)
        self.OUTPUT.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk(screenName="Calculator", baseName="Calculator", className="Calculator")
# root.geometry("320x180")
root.minsize(320, 40)
app = Application(root)
app.mainloop()
