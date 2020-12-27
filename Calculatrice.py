import tkinter
from functools import partial

police = ("Courrier", 20)

class Calculatrice:

    expr = []

    def __init__(self, master=tkinter.Tk()):
        self.master = master
        self.create_frame()
        self.configure()
        self.create_button()
        self.master.mainloop()

    def configure(self):
        self.master.title("calculatrice")
        self.master.geometry("400x600")

    def create_frame(self):
        self.frame0 = tkinter.Frame(self.master, bg="yellow", bd=20)
        self.frame0.pack(expand=tkinter.YES)

        self.frame1 = tkinter.Frame(self.frame0, bg="blue")
        self.frame1.pack(side=tkinter.TOP, fill=tkinter.X)

        self.frame2 = tkinter.Frame(self.frame0, bg="red")
        self.frame2.pack(side=tkinter.TOP, fill=tkinter.X, pady=20, ipady=100)


    def create_button(self):

        self.label1_variable = tkinter.StringVar()
        self.label1 = tkinter.Label(self.frame1, textvariable=self.label1_variable)
        self.label1.pack(expand=tkinter.YES, fill=tkinter.X, ipadx=100, ipady=10, padx=10, pady=10)

        j=9
        for y in range(0, 3):
            for x in reversed(range(0, 3)):
                Chiffre(self.frame2, j, x, y)
                j-=1


    """
    button_0 = tkinter.Button(frame2, text="0")
    button_0.pack(side=tkinter.RIGHT, ipadx=20, ipady=20, padx=5, pady=5)

    button_1 = tkinter.Button(frame2, text="1")
    button_1.pack(side=tkinter.RIGHT, ipadx=20, ipady=20, padx=5, pady=5)
    """


class Chiffre:

    expr = []

    def __init__(self, master, chfr, x, y):
        self.chfr = chfr
        self.btn = tkinter.Button(master, text=str(chfr), command=partial(self.add_chfr_to_expr, self.chfr))
        self.btn.grid(column=x, row=y, ipadx=10, ipady=10, padx=3, pady=3)

    @classmethod
    def add_chfr_to_expr(cls, num):
        Calculatrice.expr.append(num)
        print(Calculatrice.expr)


class BoutonEgal():
    def __init__(self, master):
        self.expr = Calculatrice.expr
        self.nombres = []
        self.btn = tkinter.Button(master, text='=', command=self.calculer)
        self.btn.pack()

    def somme(self):
        total = 0
        for x in self.nombres:
            total+=x
        return total

    def differance(self):
        dif = self.nombres[-1] - self.nombres[0]
        return dif

    def multi(self):
        return self.nombres[0]*self.nombres[-1]

    def div(self):
        return self.nombres[0]/self.nombres[-1]

    def calculer(self):
        for x in self.expr:
            if x in [1, 2,3,4,5,6,7,8,9,0]:
                nombre.append(x)
            else:
                if x == '+':
                    resultat = self.somme()
                elif x == '-':
                    resultat = self.differance()
                elif x == '*':
                    resultat = self.multi()
                else:
                    resultat = self.div()
        return resultat
