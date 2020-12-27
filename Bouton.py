from functools import partial
from Calculer import Calculer
import tkinter

class Bouton:
    
    def __init__(self, master, chfr, x, y):
        self.chfr = chfr
        self.btn = tkinter.Button(master, text=str(chfr), command=partial(Calculer.add_to_expr, self.chfr))
        self.btn.grid(column=x, row=y, ipadx=10, ipady=10, padx=3, pady=3)
    



