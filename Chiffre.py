import tkinter
from functools import partial

class Chiffre:

    expr = []

    def __init__(self, master, chfr, x, y):
        self.chfr = chfr
        self.btn = tkinter.Button(master, text=str(chfr), command=partial(self.add_chfr_to_expr, self.chfr))
        self.btn.grid(column=x, row=y, ipadx=10, ipady=10, padx=3, pady=3)
    
    @classmethod
    def add_chfr_to_expr(cls, num):
        cls.expr.append(num)
        print(cls.expr)
    
    @classmethod
    def get_nb(cls):
        nb = cls.expr[:-1]
        return nb
    

