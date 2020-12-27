import tkinter
from functools import partial

class Calculatrice:

    def __init__(self, master=tkinter.Tk()):
        self.master = master
        self.create_frame()
        self.configure()
        self.create_button()
        self.master.mainloop()

    def configure(self):
        self.master.title("calculatrice")
        self.master.geometry("400x600+800+10")

    def create_frame(self):
        self.frame0 = tkinter.Frame(self.master, bg="yellow", bd=20)
        self.frame0.pack(expand=tkinter.YES)

        self.frame1 = tkinter.Frame(self.frame0, bg="blue")
        self.frame1.pack(side=tkinter.TOP, fill=tkinter.X)

        self.frame2 = tkinter.Frame(self.frame0, bg="red")
        self.frame2.pack(side=tkinter.TOP, fill=tkinter.X, pady=20, ipady=10)

    def create_button(self):

        self.label1_variable = tkinter.StringVar()
        self.label1 = tkinter.Label(self.frame1, textvariable=self.label1_variable)
        self.label1.pack(expand=tkinter.YES, fill=tkinter.X, ipadx=100, ipady=10, padx=10, pady=10)

        j=9
        for y in range(0, 3):
            for x in reversed(range(0, 3)):
                Bouton(self.frame2, j, x, y)
                j-=1
        
        c = 3
        Bouton(self.frame2, "+", c, 0)
        Bouton(self.frame2, "-", c, 1)
        Bouton(self.frame2, "*", c, 2)
        Bouton(self.frame2, "/", c, 3)
        Bouton(self.frame2, "=", c, 4)

class Bouton:

    expr = []
    
    def __init__(self, master, chfr, x, y):
        self.chfr = chfr
        self.btn = tkinter.Button(master, text=str(chfr), command=partial(self.add_to_expr, self.chfr))
        self.btn.grid(column=x, row=y, ipadx=10, ipady=10, padx=3, pady=3)

    @classmethod
    def add_to_expr(cls, num):
        cls.expr.append(num)
        Calculate.calculer()

class Calculate:

    resultat = 0

    @classmethod
    def calculer(cls):
        print(Bouton.expr)
        for x in Bouton.expr:
            if x == "+":
                cls.resultat = cls.addition()
            if x == "-":
                cls.resultat = cls.soustraction()
            if x == "*":
                cls.resultat = cls.multiplication()
            if x == "/":
                cls.resultat = cls.division()
            if x == "=":
                print(cls.resultat)
                cls.reset()
        
    @classmethod
    def addition(cls):
        return Bouton.expr[0] + Bouton.expr[-2]

    @classmethod
    def soustraction(cls):
        return Bouton.expr[0] - Bouton.expr[-2]

    @classmethod
    def multiplication(cls):
        return Bouton.expr[0] * Bouton.expr[-2]

    @classmethod
    def division(cls):
        return Bouton.expr[0] / Bouton.expr[-2]

    @classmethod
    def reset(cls):
        Bouton.expr.clear()

    

