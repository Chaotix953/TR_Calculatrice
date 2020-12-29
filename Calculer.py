

class Calculer:

    resultat = 0
    expr = []
    count_expr = 0

    @classmethod
    def add_to_expr(cls, num):
        cls.count_expr += 1
        cls.expr.append(num)
        print(cls.expr)
#       Calculatrice.var_label1.set(str(cls.expr))
        if cls.count_expr >= 2:
            if type(cls.expr[0]) is int and type(cls.expr[1]) is int:
                cls.expr[0] = str(cls.expr[0]) 
                cls.expr[0] += str(cls.expr[1])
                del cls.expr[1]
                cls.expr[0] = int(cls.expr[0])
            if type(cls.expr[-1]) is int and type(cls.expr[-2]) is int:
                cls.expr[-1] = str(cls.expr[-1]) 
                cls.expr[-1] += str(cls.expr[-2])
                del cls.expr[-2]
                cls.expr[-1] = int(cls.expr[-1])

    @classmethod
    def calculer(cls):
        print(cls.expr)
        for x in cls.expr:
            if str(x) == "+":
                cls.resultat = cls.addition()
            if x == "-":
                cls.resultat = cls.soustraction()
            if x == "*":
                cls.resultat = cls.multiplication()
            if x == "/":
                cls.resultat = cls.division()
        print("Le résultat est", cls.resultat)
        #cls.reset()
        cls.expr = str(cls.resultat)

    @classmethod
    def addition(cls):
        return float(cls.expr[0]) + float(cls.expr[-1])

    @classmethod
    def soustraction(cls):
        return float(cls.expr[0]) - float(cls.expr[-1])

    @classmethod
    def multiplication(cls):
        return float(cls.expr[0]) * float(cls.expr[-1])

    @classmethod
    def division(cls):
        return float(cls.expr[0]) / float(cls.expr[-1])

    @classmethod
    def reset(cls):
        cls.expr = []
        cls.count_expr = 0
        print("CLEAR")
