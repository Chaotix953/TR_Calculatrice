

class Calculer:

    resultat = 0
    expr = []

    @classmethod
    def add_to_expr(cls, num):
        cls.expr.append(num)
        print(cls.expr)
        #cls.calculer()

    @classmethod
    def calculer(cls):
        print(cls.expr)
        for x in cls.expr:
            if x == "+":
                cls.resultat = cls.addition()
                print(cls.resultat)
            if x == "-":
                cls.resultat = cls.soustraction()
            if x == "*":
                cls.resultat = cls.multiplication()
            if x == "/":
                cls.resultat = cls.division()
#            if x == "=":
#                print(cls.resultat)
#                cls.reset()

    @classmethod
    def addition(cls):
        return float(cls.expr[0]) + float(cls.expr[-1])

    @classmethod
    def soustraction(cls):
        return float(cls.expr[0]) - float(cls.expr[-1])

    @classmethod
    def multiplication(cls):
        return float(cls.expr[0]) * float(cls.expr[-2])

    @classmethod
    def division(cls):
        return float(cls.expr[0]) / float(cls.expr[-2])

    @classmethod
    def reset(cls):
        cls.expr.clear()