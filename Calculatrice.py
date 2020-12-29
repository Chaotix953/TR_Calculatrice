import tkinter
from Bouton import BoutonChiffre, BoutonSign
from Calculer import Calculer

class Calculatrice:

    def __init__(self, master=tkinter.Tk()):
        self.master = master
        self.create_frame()
        self.configure()
        self.create_button()
        self.master.mainloop()

    def configure(self):
        self.master.title("Calculatrice")
        self.master.geometry("400x600+800+10")

    def create_frame(self):
        self.frame0 = tkinter.Frame(self.master, bg="yellow", bd=20)
        self.frame0.pack(expand=tkinter.YES)

        self.frame1 = tkinter.Frame(self.frame0, bg="blue")
        self.frame1.pack(side=tkinter.TOP, fill=tkinter.X)

        self.frame2 = tkinter.Frame(self.frame0, bg="red")
        self.frame2.pack(side=tkinter.TOP, fill=tkinter.X, pady=20, ipady=10)

    def update_label(self):
        expr = ''
        for x in Calculer.expr:
            expr += str(x)
        self.var_label1.set(expr)
        self. master.after(100, self.update_label)

    def create_button(self):
        self.var_label1 = tkinter.StringVar()
        self.var_label1.set('En cours de devloppement')
        self.label1 = tkinter.Label(self.frame1, textvariable=self.var_label1)
        self.label1.pack(expand=tkinter.YES, fill=tkinter.X, ipadx=30, ipady=10, padx=10, pady=10)

        j=9
        for y in range(0, 3):
            for x in reversed(range(0, 3)):
                BoutonChiffre(self.frame2, j, x, y)
                j-=1

        BoutonChiffre(self.frame2, 0, 1, 3)

        c = 3
        BoutonChiffre(self.frame2, "+", c, 0)
        BoutonChiffre(self.frame2, "-", c, 1)
        BoutonChiffre(self.frame2, "*", c, 2)
        BoutonChiffre(self.frame2, "/", c, 3)
        BoutonSign(self.frame2, "=", c, 4, Calculer.calculer)
        BoutonSign(self.frame2, "CLR", c, 5, Calculer.reset)
        self.master.after(100, self.update_label)






