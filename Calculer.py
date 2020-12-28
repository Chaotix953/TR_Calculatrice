

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
            if str(x) == "+":
                cls.resultat = cls.addition()
                print("Le résultat est", cls.resultat)
                cls.reset()
            if x == "-":
                cls.resultat = cls.soustraction()
                print("Le résultat est", cls.resultat)
                cls.reset()
            if x == "*":
                cls.resultat = cls.multiplication()
                print("Le résultat est", cls.resultat)
                cls.reset()
            if x == "/":
                cls.resultat = cls.division()
                print("Le résultat est", cls.resultat)
                cls.reset()
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
        cls.expr.clear()
