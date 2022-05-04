# --- classe

class Calculadora:
    # ----- Funcao ------
    # Metodo: não retorna valor
    # Funcao: tudo que retorna valor
    # declaracao de definição = def
    def __init__(self):
        pass

    # pass = somente preeche campo vazio

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplic(self, valor_a, valor_b):
        return valor_a * valor_b

    def divi(self, valor_a, valor_b):
        return valor_a / valor_b


# instancia de classe
calculadora = Calculadora()

print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(calculadora.divi(100, 2))
print(calculadora.multiplic(10, 5))
