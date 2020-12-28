from functools import partial
from Calculer import Calculer
import tkinter

class BoutonChiffre:

    def __init__(self, master, chfr, x, y):
        self.chfr = chfr
        self.btn = tkinter.Button(master, text=str(chfr), command=partial(Calculer.add_to_expr, self.chfr))
        self.btn.grid(column=x, row=y, ipadx=10, ipady=10, padx=3, pady=3)


class BoutonSign:
    def __init__(self, master, sign, x ,y, op):
        self.sign = sign
        self.btn = tkinter.Button(master, text=str(sign), command=op)
        self.btn.grid(column=x, row=y, ipadx=10, ipady=10, padx=3, pady=3)
