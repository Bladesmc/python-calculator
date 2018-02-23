# TODO: support multiple operations at once WHICH IS NOT EASY SO IT MIGHT NOT GET DONE

import calculations as calc
from Tkinter import *


class Application(Frame):
    def calculate(self):
        inp = self.INPUT.get()
        self.v.set(calc.calculate(inp))

    def createwidgets(self):
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
        self.createwidgets()


root = Tk(screenName="Calculator", baseName="Calculator", className="Calculator")
# root.geometry("320x180")
root.minsize(320, 40)
root.maxsize(1920, 1080)
app = Application(root)
app.mainloop()
